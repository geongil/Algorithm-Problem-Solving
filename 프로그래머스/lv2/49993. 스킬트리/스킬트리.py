def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for i in range(len(skill_trees)):
        skill_book = list(skill)
        skills = list(skill_trees[i])
        print(skills)
        for j in range(len(skills)):
            if skills[j] in skill_book:
                if skills[j] == skill_book[0]:
                    skill_book.pop(0)
                else:
                    answer -= 1
                    break           
            else:
                continue
        
    return answer