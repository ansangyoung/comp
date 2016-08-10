from comp_datasort_functions import *

datasort_map = [
    ('번호순', number_sort),
    ('이름순', name_sort),
    ('점수내림차순', score_reverse_sort),
    ('점수오름차순', score_sort),
]

datasort_list = [x[0] for x in datasort_map]
