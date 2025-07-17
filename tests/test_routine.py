"""
Unit tests for a project's program's routine objects.  :)
"""

from tests import fixture
import unittest

class Routines(unittest.TestCase):
    def setUp(self):
        prj = fixture.string_to_project('''
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>                                    
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
            <Program Use="Context" Name="Main" Class="Standard">
                <Routines Use="Context">
                    <Routine Use="Target" Name="Sample_Routine" Type="RLL">
                        <RLLContent>
                            <Rung Number="0" Type="N">
                                <Text>
                                <![CDATA[NOP();]]>
                                </Text>
                            </Rung>
                            <Rung Number="1" Type="N">
                                <Comment>
                                    <![CDATA[Manual Mode]]>
                                </Comment>
                                <Text>
                                    <![CDATA[[XIC(Manual_PB) ,XIC(Manual_Mode) ]XIC(Safety.OK)XIO(Reset_PB)XIO(Automatic_PB)OTE(Manual_Mode);]]>
                                </Text>
                            </Rung>
                                <Rung Number="2" Type="N">
                                <Comment>
                                    <![CDATA[Automatic Mode]]>
                                </Comment>
                                <Text>
                                    <![CDATA[[XIC(Automatic_PB) ,XIC(Automatic_Mode) ]XIC(Safety.OK)XIO(Reset_PB)XIO(Manual_PB)OTE(Automatic_Mode);]]>
                                </Text>
                            </Rung>
                        </RLLContent>
                    </Routine>
                </Routines>
            </Program>
        </Programs>
    </Controller>
</RSLogix5000Content>''')
        program = prj.programs["Main"]
        self.routine = program.routines['Sample_Routine']


    def test_1(self):
        pass




        