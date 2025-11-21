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


