import time

# 테스트 데이터: 전역 변수
TEST_CASES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

def factorial_iter(n: int) -> int:
    """
    반복문을 사용하여 n! (팩토리얼)을 계산합니다.
    """
    if n < 0:
        raise ValueError("n은 0 이상의 정수여야 합니다.")
    
    result = 1
    for k in range(1, n + 1):
        result *= k
    return result

def factorial_rec(n: int) -> int:
    """
    재귀 호출을 사용하여 n! (팩토리얼)을 계산합니다.
    """
    if n < 0:
        raise ValueError("n은 0 이상의 정수여야 합니다.")

    if n <= 1:
        return 1
    else:
        return n * factorial_rec(n - 1)

def run_with_time(func, n):
    """
    주어진 함수의 실행 시간을 측정합니다.
    """
    try:
        start_time = time.perf_counter()
        result = func(n)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return result, elapsed_time
    except (ValueError, RecursionError) as e:
        print(f"오류 발생: {e}")
        return None, None

def run_batch_tests():
    """
    미리 정의된 테스트 케이스들에 대해 일괄적으로 팩토리얼 계산을 수행합니다.
    """
    print("\n[테스트 데이터 실행]")
    for n in TEST_CASES:
        iter_result, iter_time = run_with_time(factorial_iter, n)
        rec_result, rec_time = run_with_time(factorial_rec, n)

        if iter_result is None or rec_result is None:
            print(f"{n} | 테스트 실패")
            continue
        
        print(f"{n}! = {iter_result}")
        is_match = (iter_result == rec_result)
        print(f"{n} | same={is_match} | iter={iter_time:.6f}s, rec={rec_time:.6f}s")

def get_positive_integer_input(prompt_message: str) -> int | None:
    """
    사용자로부터 0 이상의 정수 입력을 받고, 변환에 실패하면 None을 반환합니다.
    """
    try:
        n_str = input(prompt_message)
        n = int(n_str)
        if n < 0:
            print("정수(0 이상의 숫자)만 입력하세요.")
            return None
        return n
    except ValueError:
        print("정수(0 이상의 숫자)만 입력하세요.")
        return None

def main():
    """
    메인 함수. 인터랙티브 메뉴를 표시하고 사용자 입력을 처리합니다.
    """
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.")
    
    while True:
        print("\n============= Factorial Tester =============")
        print("1) 반복법으로 n! 계산")
        print("2) 재귀로 n! 계산")
        print("3) 두 방식 모두 계산 후 결과/시간 비교")
        print("4) 준비된 테스트 데이터 일괄 실행")
        print("q) 종료")
        print("==========================================")
        
        choice = input("선택: ")

        if choice == '1' or choice == '2':
            n = get_positive_integer_input("n 값(정수, 0 이상)을 입력하세요 : ")
            if n is not None:
                func = factorial_iter if choice == '1' else factorial_rec
                name = "반복" if choice == '1' else "재귀"
                result, elapsed_time = run_with_time(func, n)
                if result is not None:
                    print(f"[{name}] {n}! = {result}")

        elif choice == '3':
            n = get_positive_integer_input("n 값(정수, 0 이상)을 입력하세요 : ")
            if n is not None:
                iter_result, iter_time = run_with_time(factorial_iter, n)
                rec_result, rec_time = run_with_time(factorial_rec, n)

                if iter_result is not None and rec_result is not None:
                    print(f"[반복] {n}! = {iter_result}")
                    print(f"[재귀] {n}! = {rec_result}")
                    match_status = "일치" if iter_result == rec_result else "불일치"
                    print(f"결과 일치 여부: {match_status}")
                    print(f"[반복] 시간: {iter_time:.6f} s | [재귀] 시간: {rec_time:.6f} s")

        elif choice == '4':
            run_batch_tests()

        elif choice.lower() == 'q':
            print("종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()