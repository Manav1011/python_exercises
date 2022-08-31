import os

class select_notes:
    def __init__(self):
        self.notes={
            'AJAVA':{
                'unit 1':r'D:\sem-6\Ajava\ajava_practicals\ajava_notes\3360701_AJAVA_GTU_Study_Material_e-Notes_Unit-1_03082019051906AM.pdf',
                'unit 2':r'D:\sem-6\Ajava\ajava_practicals\ajava_notes\3360701_AJAVA_GTU_Study_Material_e-Notes_Unit-2_03082019052236AM.pdf',
                'unit 3':r'D:\sem-6\Ajava\ajava_practicals\ajava_notes\3360701_AJAVA_GTU_Study_Material_e-Notes_Unit-3_03082019052343AM.pdf',
                'unit 4':r'D:\sem-6\Ajava\ajava_practicals\ajava_notes\3360701_AJAVA_GTU_Study_Material_e-Notes_Unit-4_03082019052914AM.pdf',
                'unit 5':r'D:\sem-6\Ajava\ajava_practicals\ajava_notes\3360701_AJAVA_GTU_Study_Material_e-Notes_Unit-5_03082019052452AM.pdf',
                'amit sir unit 1':r'D:\sem-6\Ajava\ajava_practicals\ajava_notes\Unit 1 Solutions.pdf',
                'amit sir unit 2':r"D:\sem-6\Ajava\ajava_practicals\ajava_notes\Unit 2_Solution.pdf",
                'differences':r"D:\sem-6\Ajava\ajava_practicals\ajava_notes\difference all.pdf",
                'Summer-2019':r"D:\sem-6\Ajava\question papers\s-2019.pdf",
                'Summer 2020':r"D:\sem-6\Ajava\question papers\s-2020.pdf",
                'Summer 2021':r"D:\sem-6\Ajava\question papers\s-2021.pdf",
                'Winter 2019':r"D:\sem-6\Ajava\question papers\w-2019.pdf",
                'Winter 2020':r"D:\sem-6\Ajava\question papers\w-2020.pdf",
                'Winter 2021':r"D:\sem-6\Ajava\question papers\w-2021.pdf",
                    },
            'NMA':{
                'CH 1 & 2':r"D:\sem-6\NMA\CE6_NMA_Notes.pdf",
                'CH 3 & 4':r"D:\sem-6\NMA\CE_NMA_Lecture Notes Chapter 3,4.pdf",
                'Winter 2020':r"D:\sem-6\NMA\gtu-papers\3360703-DIPLOMA-WINTER-2020.pdf",
                'Winter 2021':r"D:\sem-6\NMA\gtu-papers\3360703-DIPLOMA-WINTER-2021.pdf",
                'Summer 2019':r"D:\sem-6\NMA\gtu-papers\3360703-DIPLOMA-SUMMER-2019.pdf",
                'Summer 2020':r"D:\sem-6\NMA\gtu-papers\3360703-DIPLOMA-SUMMER-2020.pdf",
                'Summer 2021':r"D:\sem-6\NMA\gtu-papers\3360703-DIPLOMA-SUMMER-2021.pdf",
                'Winter 2019':r"D:\sem-6\NMA\gtu-papers\3360703-DIPLOMA-WINTER-2019.pdf",
            },
            'MCAD':{
                'Mcad book notes':r"D:\sem-6\mcad\MCAD_ Book_Notes.pdf",
                'MCAD Chapter 1 Notes':r'"D:\sem-6\mcad\Unit-1_MCAD_VPMP.pdf"',
                'MCAD Chapter 2 Notes':r'"D:\sem-6\mcad\Unit-2-MCAD_VPMP.pdf"',
                'MCAD Chapter 3 Notes':r'"D:\sem-6\mcad\Unit-3-MCAD_VPMP.pdf"',
                'MCAD Chapter 4 Notes':r'"D:\sem-6\mcad\Unit-4-MCAD_VPMP.pdf"',
                'MCAD Chapter 5 notes:':r'"D:\sem-6\mcad\Unit-5-MCAD_VPMP.pdf"',
                'Summer 2019':r"D:\sem-6\mcad\gtu-papers\3360704-DIPLOMA-SUMMER-2019.pdf",
                'Summer 2020':r"D:\sem-6\mcad\gtu-papers\3360704-DIPLOMA-SUMMER-2020.pdf",
                'Summer 2021':r"D:\sem-6\mcad\gtu-papers\3360704-DIPLOMA-SUMMER-2021.pdf",
                'Winter 2019':r"D:\sem-6\mcad\gtu-papers\3360704-DIPLOMA-WINTER-2019.pdf",
                'Winter 2020':r"D:\sem-6\mcad\gtu-papers\3360704-DIPLOMA-WINTER-2020.pdf",
                'Winter 2021':r"D:\sem-6\mcad\gtu-papers\3360704-DIPLOMA-WINTER-2021.pdf"
            },
            'practical list':{
                'practical_list':r"D:\PRACTICAL-LIST.pdf"
             }
        }
    def select(self):
        while True:
            count=0
            count_dict={}
            for i in self.notes.keys():
                print(count,':',i)
                count_dict.update({count:i})
                count+=1
            print()
            sub_selection=int(input("Select the number according to the subject you want to select: "))
            os.system("cls")
            sub_value=count_dict[sub_selection]
            count=0
            count_dict.clear()
            for i in self.notes[sub_value].keys():
                count_dict.update({count:i})
                count+=1
            while True:
                for i,j in count_dict.items():
                    print(i," : ",j)
                print()
                note_selection=int(input("Select the number according to the subject you want to select: "))
                os.system("cls")
                if note_selection in count_dict.keys():
                    unit_value=count_dict[note_selection]
                    note_value=self.notes[sub_value][unit_value]
                    os.startfile(note_value)
                    continue
                else:
                    break
                
            continue
        
a=select_notes()
a.select()