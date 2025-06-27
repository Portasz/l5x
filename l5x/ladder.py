from .rung import Rung
from .rung_factory import RungFactory



class Ladder:
    def __init__(self, element, rungs=None):
        self._rungs = rungs or []
        self.element = element
    
    def add_rung(self, rung=None, index=None):
        """Add a rung at specified index or append to end"""
        if rung is None:
            rung = RungFactory.create_rung()

        if index is None:
            self._rungs.append(rung)
            rung.number = len(self._rungs) - 1  # sets index to end of array
        else:
            converted_index = self._convert_insert_index(index)
            self._rungs.insert(converted_index, rung)
            self.update_rung_numbers(converted_index)

        self.element.insert(int(rung.number), rung.element)
        return rung
    
    def remove_rung(self, index):
        """Remove rung at index"""
        '''convert the index right away in this function to fix a bug when accessing index 0 through negative means'''
        converted_index = self._convert_access_index(index) 
        retval = self._rungs.pop(converted_index)
        self.update_rung_numbers(converted_index)

        self.element.remove(retval.element) #remove the rung from the xml tree
        return retval
    
    def move_rung(self, source_index, destination_index):
        """Move rung from one position to another"""
        converted_source_index = self._convert_access_index(source_index)
        converted_destination_index = self._convert_insert_index(destination_index)
        
        if converted_destination_index > converted_source_index:
            converted_destination_index -= 1

        #ladder list logic
        rung = self._rungs.pop(converted_source_index)
        self._rungs.insert(converted_destination_index, rung)
        
        #xml element logic
        self.element.remove(rung.element)
        self.element.insert(converted_destination_index,rung.element)

        
        self.update_rung_numbers(start_index=min(converted_source_index,converted_destination_index))
    
    def find_rung_by_comment(self, comment):
        """Find rungs containing specific comment"""
        return [i for i, rung in enumerate(self._rungs) 
                if comment in getattr(rung, 'comment', '')]
    
    #updates the rung number attributes stored in each rung based on list position 
    def update_rung_numbers(self, start_index=0):
        
        #avoids edge cases where update is called on the end of a list after the last index was removed
        if start_index == len(self._rungs):
            return

        converted_start_index = self._convert_access_index(start_index)
        for index, rung in enumerate(self._rungs[start_index:], start=converted_start_index):
            rung.number = index


    def __iter__(self):
        return iter(self._rungs)
    
    def __len__(self):
        return len(self._rungs)
    
    def __getitem__(self, index):
        return self._rungs[index]

    def _convert_access_index(self, index):
        """Convert negative indices for access/removal."""
        if index < 0:
            index += len(self._rungs)
        if index < 0 or index >= len(self._rungs):
            raise IndexError(f"Rung index out of range. Index: {index} Length: {len(self._rungs)}")
        return index

    def _convert_insert_index(self, index):
        """Convert negative indices for insertion."""
        if index < 0:
            index += len(self._rungs) + 1
        if index < 0 or index > len(self._rungs):
            raise IndexError(f"Rung insert index out of range. Index: {index} Length: {len(self._rungs)}")
        return index











