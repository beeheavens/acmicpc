# 최대 일차 일변수 다항식이 주어진다.
# 즉, 주어지는 입력은 ax + b 혹은 ax라는 것
# 그렇다면 꼭 더하기일까??
# 해야 할 것
# 1. 항이 하나인지 두개인지 파악
# 2. 항이 두개라면 +인지 - 인지 파악 (곱셈과 나눗셈은 배제)
# 3. 적분
# 4. 적분상수 출력

formula = input() # 주어진 일차 일변수 다항식

# 아 안해준게있다.
# 1이면 출력하지 말아야 하는데

if formula == '0':
    print('W')
else:
    #항이 하나인지 두개인지 결정 맨 앞에 -가 붙을 수 있으니 제하고 생각
    if '+' in formula: # 항이 두개, +
        parsed = []
        plus_pos = formula.index('+') # + 의 위치
        parsed.append(formula[:plus_pos-1]) # x의 계수 저장
        parsed.append('+')
        parsed.append(formula[plus_pos+1:]) # 상수항 저장
        first_g = int(parsed[0])//2 # 적분 후 이차항의 계수
        second_g = int(parsed[2]) # 적분 후 일차항의 계수
        if first_g == 1:
            first = 'xx'
        elif first_g == -1:
            first = '-xx'
        else:
            first = f"{first_g}xx"
        if second_g == 1:
            second = 'x'
        elif second_g == -1:
            second = '-x'
        else:
            second = f"{second_g}x"
        print(f"{first}{parsed[1]}{second}+W")
    elif '-' in formula[1:]: # 맨 앞이 -일수 있으므로
        minus_pos = formula[1:].index('-') + 1
        parsed = []
        parsed.append(formula[:minus_pos-1]) # x의 계수 저장
        parsed.append('-')
        parsed.append(formula[minus_pos+1:]) # 상수항 저장
        first_g = int(parsed[0])//2 # 적분 후 이차항의 계수
        second_g = int(parsed[2]) # 적분 후 일차항의 계수
        if first_g == 1:
            first = 'xx'
        elif first_g == -1:
            first = '-xx'
        else:
            first = f"{first_g}xx"
        if second_g == 1:
            second = 'x'
        elif second_g == -1:
            second = '-x'
        else:
            second = f"{second_g}x"
        print(f"{first}{parsed[1]}{second}+W")
    else: # 항이 하나인 경우
        if 'x' in formula : #일차항 하나만 있는 경우
            x_pos = formula.index('x')
            g = int(formula[:x_pos])//2 # 적분 시 계수
            if g == 1:
                print("xx+W")
            elif g == -1:
                print("-xx+W")
            else:
                print(f"{g}xx+W")
        else: #상수항 하나인 경우
            g = int(formula)
            if g == 1:
                print("x+W")
            elif g == -1:
                print("-x+W")
            else:
                print(f"{g}x+W")
            
        