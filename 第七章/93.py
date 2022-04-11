
def selection_sort(lst: list, reverse=False):
    for i in range(len(lst)):
        m_index = i
        for j in range(i, len(lst)):
            if isinstance(lst[j], str) and isinstance(lst[m_index], str):
                if reverse:
                    if ord(lst[j]) > ord(lst[m_index]):
                        m_index = j
                else:
                    if ord(lst[j]) < ord(lst[m_index]):
                        m_index = j
            # else:
            #     if reverse:
            #         if lst[j] > lst[m_index]:
            #             m_index = j
            #     else:
            #         if lst[j] < lst[m_index]:
            #             m_index = j
        lst[i], lst[m_index] = lst[m_index], lst[i]


if __name__ == "__main__":
    character = list(input())
    selection_sort(character)
    print(character)

    selection_sort(character, reverse=True)
    print(character)
