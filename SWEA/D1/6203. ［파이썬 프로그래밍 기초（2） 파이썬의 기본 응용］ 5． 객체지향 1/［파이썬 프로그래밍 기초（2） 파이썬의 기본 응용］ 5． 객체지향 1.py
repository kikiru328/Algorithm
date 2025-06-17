scores = tuple(map(int, input().split(',')))
class Result:
    def __init__(self, scores: tuple):
        self.korean: int = scores[0]
        self.english: int = scores[1]
        self.math: int = scores[2]
        
    def get_total_score(self) -> int:
        return sum((self.korean, self.english, self.math))
    
student = Result(scores)
print(f"국어, 영어, 수학의 총점: {student.get_total_score()}")
        