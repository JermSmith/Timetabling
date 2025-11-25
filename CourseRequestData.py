import csv
import Helper

class RequestedCourse():
    def __init__(self, 
                 course_code, 
                 sem_0_req_count, 
                 sem_1_req_count, 
                 sem_2_req_count, 
                 gr_9_req_count, 
                 gr_10_req_count, 
                 gr_11_req_count, 
                 gr_12_req_count, 
                 num_sections_needed):
        
        
        self._course_code = course_code
        
        
        self._sem_0_request_count = sem_0_req_count
        self._sem_1_request_count = sem_1_req_count
        self._sem_2_request_count = sem_2_req_count
        
        
        self._grade_09_request_count = gr_9_req_count
        self._grade_10_request_count = gr_10_req_count
        self._grade_11_request_count = gr_11_req_count
        self._grade_12_request_count = gr_12_req_count
        
        
        self._num_sections_needed = num_sections_needed
        
        
        # determine whether it is a grade 9, 10, 11, or 12 course
        self._listed_grade = -1
        grade_code = self._course_code[-2]
        if grade_code not in ["1", "2", "3", "4"]:
            print(f"Warning: Course code of {self._course_code} doesn't match expected formatting for grade_code (e.g. 2G, 3S).")
            raise RuntimeError
        else:
            self._listed_grade = int(grade_code) + 8 # 1->9, 4->12
        
        
        # determine whether there are many grade (n-1)'s enrolled in this grade n class.
        # if so, we will prioritize its prerequisites in 1st semester
        self._lower_grades_overrepresented = False
        
        if self._listed_grade == 11:
            if self._grade_10_request_count >= self._grade_11_request_count / 3:
                self._lower_grades_overrepresented = True
        elif self._listed_grade == 12:
            if self._grade_11_request_count >= self._grade_12_request_count / 3:
                self._lower_grades_overrepresented = True
        
        
        # keep track of prerequisite courses, for those courses that have many students of lower grades taking them
        self._prereq_courses = []
        
                
        

    def __repr__(self):
        course_request_info = "Code: " + self._course_code + "\n"
        
        course_request_info += "Sem 0 req: " + str(self._sem_0_request_count) + "\n"
        course_request_info += "Sem 1 req: " + str(self._sem_1_request_count) + "\n"
        course_request_info += "Sem 2 req: " + str(self._sem_2_request_count) + "\n"
        
        course_request_info += "Gr 09 req: " + str(self._grade_09_request_count) + "\n"
        course_request_info += "Gr 10 req: " + str(self._grade_10_request_count) + "\n"
        course_request_info += "Gr 11 req: " + str(self._grade_11_request_count) + "\n"
        course_request_info += "Gr 12 req: " + str(self._grade_12_request_count) + "\n"
        
        course_request_info += "Num sections needed: " + str(self._num_sections_needed) + "\n"
        
        return course_request_info
    
    def __str__(self):
        course_request_info = "Code: " + self._course_code + "\n"
        
        course_request_info += "Sem 0 req: " + str(self._sem_0_request_count) + "\n"
        course_request_info += "Sem 1 req: " + str(self._sem_1_request_count) + "\n"
        course_request_info += "Sem 2 req: " + str(self._sem_2_request_count) + "\n"
        
        course_request_info += "Gr 09 req: " + str(self._grade_09_request_count) + "\n"
        course_request_info += "Gr 10 req: " + str(self._grade_10_request_count) + "\n"
        course_request_info += "Gr 11 req: " + str(self._grade_11_request_count) + "\n"
        course_request_info += "Gr 12 req: " + str(self._grade_12_request_count) + "\n"
        
        course_request_info += "Num sections needed: " + str(self._num_sections_needed) + "\n"
        
        return course_request_info


    def total_num_requests(self):
        return self._grade_09_request_count + self._grade_10_request_count +\
        self._grade_11_request_count + self._grade_12_request_count
        
    def code(self):
        return self._course_code

    def num_sections_needed(self):
        return self._num_sections_needed
    
    def listed_grade(self):
        return self._listed_grade
    
    def add_prereq_courses_if_lower_grades_overrepresented(self, all_course_codes):
        if self._lower_grades_overrepresented:
            print(f"The course {self._course_code}, a grade {self._listed_grade} course, has many grade {self._listed_grade - 1} students enrolled. Please list this course's prerequisites that these grade {self._listed_grade - 1} students will need to take in 1st semester.")
            more_prereq_to_input = True
            while more_prereq_to_input:
                prereq_code = input(f"Enter a course code for a prereq for {self._course_code} 'stop' to stop: ")
                if prereq_code not in all_course_codes:
                    print("Invalid course code. Try again.")
                elif prereq_code in self._prereq_courses:
                    print("Course already added to prereqs. Try again.")
                elif prereq_code.lower().strip() == "stop":
                    more_prereq_to_input = False
                else:
                    self._prereq_courses.append(prereq_code)
        
                    
        

class CourseRequestData():
    def __init__(self):
        self._requests_csv_file = open('CourseRequests.csv', newline='')
        self._requests_csv_reader = csv.reader(self._requests_csv_file, delimiter=',', quotechar='"')
        
        self._all_course_codes_list = []
        self._requested_courses_dict = {} # key: course code (str); value: RequestedCourse object

        for row in self._requests_csv_reader:
            course_code = row[0].upper().strip()
            if course_code == "﻿COURSE":
                continue
            
            sem_0_request_count = Helper.to_int(row[1].strip())
            sem_1_request_count = Helper.to_int(row[2].strip())
            sem_2_request_count = Helper.to_int(row[3].strip())
            
            gr_09_request_count = Helper.to_int(row[4].strip())
            gr_10_request_count = Helper.to_int(row[5].strip())
            gr_11_request_count = Helper.to_int(row[6].strip())
            gr_12_request_count = Helper.to_int(row[7].strip())
            
            num_sections_needed = Helper.to_int(row[8].strip())
            
            self._all_course_codes_list.append(course_code)
            
            self._requested_courses_dict[course_code] = RequestedCourse(course_code,
                                                                        sem_0_request_count,
                                                                        sem_1_request_count,
                                                                        sem_2_request_count,
                                                                        gr_09_request_count,
                                                                        gr_10_request_count,
                                                                        gr_11_request_count,
                                                                        gr_12_request_count,
                                                                        num_sections_needed)

    def get_requested_course(self, course_code):
        return self._requested_courses_dict[course_code]
    

    def get_course_requests_by_grade(self, course_code, grade):
        ...


    def print_all_course_codes(self, print_style):
        if print_style == Helper.PrintStyle.Raw:
            print(self._all_course_codes_list)
        
        elif print_style == Helper.PrintStyle.NewLine:
            for course_code in self._all_course_codes_list:
                print(course_code)
        
        else:
            print(f"Invalid PrintStyle {print_style} in print_all_course_codes")


    def print_all_requested_course_data(self, print_style):
        if print_style == Helper.PrintStyle.Raw:
            print(self._requested_courses_dict)
        
        elif print_style == Helper.PrintStyle.NewLine:
            for requested_course in self._requested_courses_dict:
                print(self._requested_courses_dict[requested_course])
        
        else:
            print(f"Invalid PrintStyle {print_style} in print_all_requested_course_data")
        
if __name__ == "__main__":
    course_req_data = CourseRequestData()
    course_req_data.print_all_requested_course_data(Helper.PrintStyle.Raw)
    print()
    course_req_data.print_all_requested_course_data(Helper.PrintStyle.NewLine)


