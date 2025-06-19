"""
Unit tests for a project's program's routine objects.  :)
"""

from tests import fixture
import unittest

class Routines(unittest.TestCase):
    def setUp(self):
        prj = fixture.string_to_project(r'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>                                    
<RSLogix5000Content SchemaRevision="1.0" SoftwareRevision="33.00" TargetName="CompactLogix" TargetType="CompactLogix" ContainsContext="false" Owner="Rockwell Automation/RSLogix 5000" ExportDate="Wed Jun 18 10:30:00 2025" ExportOptions="References NoRawData L5KData DecoratedData Context Dependencies ForceProtectedEncoding AllProjDocTrans">
<Controller Use="Context" Name="TestController">
<DataTypes Use="Context">
</DataTypes>
<Modules Use="Context">
</Modules>
<Tags Use="Context">
<Tag Name="Motor_Start" TagType="Base" DataType="BOOL" Usage="Output"/>
<Tag Name="Motor_Stop" TagType="Base" DataType="BOOL" Usage="Input"/>
<Tag Name="System_Ready" TagType="Base" DataType="BOOL" Usage="Internal"/>
<Tag Name="Timer_1" TagType="Base" DataType="TIMER" Usage="Internal"/>
</Tags>
<Programs Use="Context">
<Program Use="Context" Name="MainProgram">
<Tags Use="Context">
</Tags>
<Routines Use="Context">
<Routine Use="Context" Name="MainRoutine" Type="RLL">
<RLLContent>
<Rung Number="0" Type="N">
<Comment>
<![CDATA[Motor control logic - Start/Stop with safety interlock]]>
</Comment>
<Text>
<![CDATA[XIC(Motor_Stop)XIO(System_Ready)OTE(Motor_Start);]]>
</Text>
</Rung>
<Rung Number="1" Type="N">
<Text>
<![CDATA[XIC(Motor_Start)TON(Timer_1,5000,0);]]>
</Text>
</Rung>
<Rung Number="2" Type="N">
<Comment>
<![CDATA[System ready indication with timer delay]]>
</Comment>
<Text>
<![CDATA[XIC(Timer_1.DN)OTE(System_Ready);]]>
</Text>
</Rung>
<Rung Number="3" Type="N">
<Text>
<![CDATA[XIC(System_Ready)XIC(Motor_Start)OTE(Motor_Start);]]>
</Text>
</Rung>
<Rung Number="4" Type="N">
<Comment>
<![CDATA[Emergency stop - immediate shutdown]]>
</Comment>
<Text>
<![CDATA[XIC(Motor_Stop)OTU(Motor_Start)OTU(System_Ready);]]>
</Text>
</Rung>
<Rung Number="5" Type="N">
<Text>
<![CDATA[NOP();]]>
</Text>
</Rung>
</RLLContent>
</Routine>
</Routines>
</Program>
</Programs>
</Controller>
</RSLogix5000Content>''')
        program = prj.programs["MainProgram"]
        self.routine = program.routines['MainRoutine']


    def test_1(self):
        pass




        