# Importent | Medium level
"""
Problem: Sort List Of Dicts By Key
Topics: List, Hash Map
"""
class Solution:
    def bubble_sort_dicts(self, data_list, key) -> list[dict]:
        n = len(data_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data_list[j][key] > data_list[j + 1][key]:
                    data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
        return data_list

if __name__ == "__main__":
    solution = Solution()
    my_list_of_dicts = [
        {'vCaseType': '12', 'vCaseNo': '2451', 'vCaseYear': '2016'},
        {'vCaseType': '15', 'vCaseNo': '5871', 'vCaseYear': '2018'},
        {'vCaseType': '11', 'vCaseNo': '1542', 'vCaseYear': '2010'},
        {'vCaseType': '9', 'vCaseNo': '3651', 'vCaseYear': '2019'},
        {'vCaseType': '21', 'vCaseNo': '8139', 'vCaseYear': '2003'},
        {'vCaseType': '6', 'vCaseNo': '2142', 'vCaseYear': '2024'},
        {'vCaseType': '3', 'vCaseNo': '4547', 'vCaseYear': '2022'},
        {'vCaseType': '51', 'vCaseNo': '9754', 'vCaseYear': '2011'},
        {'vCaseType': '84', 'vCaseNo': '3536', 'vCaseYear': '2008'}
    ]

    sorted_list = solution.bubble_sort_dicts(my_list_of_dicts, "vCaseNo")
    print(sorted_list)