import csv
import Helper

class InitialTeacherTeamData():
    def __init__(self):
        self._teacher_csv_file = open('teacher_list.csv', newline='')
        self._teacher_csv_reader = csv.reader(self._teacher_csv_file, delimiter=',', quotechar='"')

        self._all_teachers_names_list = [] # list of all teachers' names
        self._all_teams_list = [] # list of all teams (not associated with any teacher here)

        self._teacher_teams_dictionary = {} # key: teacher's name; value: list of teams that teacher can teach

        for row in self._teacher_csv_reader:
            teacher_name_str = row[0].strip().upper()
            teacher_teams_list = row[1].split(",")
            
            if teacher_name_str == "TEACHER":
                continue
            
            self._all_teachers_names_list.append(teacher_name_str)
            
            for i in range(len(teacher_teams_list)):
                teacher_teams_list[i] = teacher_teams_list[i].strip().upper()
                
                team = teacher_teams_list[i]
                if team not in self._all_teams_list:
                    self._all_teams_list.append(team)
            
            self._teacher_teams_dictionary[teacher_name_str] = teacher_teams_list

    def get_all_teacher_names_list(self):
        return self._all_teachers_names_list
    
    def get_all_teams_list(self):
        return self._all_teams_list
    
    def get_teacher_teams_dictionary(self):
        return self._teacher_teams_dictionary
    
    def get_teams_of_teacher(self, teacher):
        teacher = teacher.upper().strip()
        
        try:
            return self._teacher_teams_dictionary[teacher]
        except KeyError as e:
            print(f"KeyError: {e} not found in self._teacher_teams_dictionary")
        except Exception as e:
            print(f"Unhandled Exception in get_teams_of_teacher: {e}")
            
    def get_all_teachers_on_team(self, team):
        team = team.upper().strip()
        
        if team not in self._all_teams_list:
            print(f"Invalid team provided in get_teachers_on_team: {team}")
            return
        
        teachers_on_team = []
        for teacher in self._teacher_teams_dictionary:
            if team in self._teacher_teams_dictionary[teacher]:
                teachers_on_team.append(teacher)
        return teachers_on_team
        
    def teacher_is_on_team(self, teacher, team):
        teacher = teacher.upper().strip()
        team = team.upper().strip()
        
        teams = self.get_teams_of_teacher(teacher)
        if team in teams:
            return True
        return False
    
    def print_all_teacher_names(self, print_style):
        if print_style == Helper.PrintStyle.Raw:
            print(self._all_teachers_names_list)
            
        elif print_style == Helper.PrintStyle.NewLine:
            for teacher in self._all_teachers_names_list:
                print(teacher)
        else:
            print(f"Invalid print style {print_style} in print_all_teacher_names.")
    
    def print_all_teams(self, print_style):
        if print_style == Helper.PrintStyle.Raw:
            print(self._all_teams_list)
            
        elif print_style == Helper.PrintStyle.NewLine:
            for team in self._all_teams_list:
                print(team)
                
        else:
            print(f"Invalid print style {print_style} in print_all_teams.")
    
    def print_all_teachers_with_respective_teams(self, print_style):
        if print_style == Helper.PrintStyle.Raw:
            for teacher in self._teacher_teams_dictionary:
                print(teacher, self._teacher_teams_dictionary[teacher])
        
        elif print_style == Helper.PrintStyle.NewLine:
            for teacher in self._teacher_teams_dictionary:
                print(teacher)
                for team in self._teacher_teams_dictionary[teacher]:
                    print(team)
                print()



if __name__ == "__main__":
    test_object = InitialTeacherTeamData()
    






