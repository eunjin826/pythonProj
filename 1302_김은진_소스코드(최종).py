# 1. 계획세우기
# 2. lucky(color,number)
# 3. 격언
# 4. 건강(긴장,스트레스,상담)
# 5. 공부팁

from datetime import datetime
import time
import random
number = random.randrange(1,6) # 1~5사이의 랜덤 숫자
c = ['빨간색','주황색','노란색','초록색','파란색','보라색','분홍색','고동색','검은색','하얀색','잿빛색']
color = random.choice(c) # 랜덤 색깔
m=["당신이 있는 그곳에서 시작하라. 당신이 가진 그것을 사용하라. -아서 애시-","잘하도록, 더 잘하도록, 가장 잘하도록 절대로 쉬지 말라. 잘하는 것이 더 잘하게 되고, 더 잘하는 것이 최고가 되기까지. -성 제롬-","희망은 인간을 성공으로 인도하는 신앙이다. 희망이 없으면, 아무 것도 이룰 수 없다. -헬렌 켈러-","언제나 최선을 다하라. 지금 심는 것을 나중에 거둘 것이다. -오그 만디노-","앞서가는 비결은 시작하는 것이다. -마크 트웨인-","시계를 보지 말라. 주어진 것을 하고 계속 쉬지 말라. -샘 레븐슨-","미루는 것은 시간 도둑이다. -에드워드 영-","많은 사람들이 기회를 놓친다. 왜냐하면 기회는 작업복을 입고 있으며, 일처럼 보여지기 때문이다. -토마스 에디슨-","야망이 성공으로 가는 길이고, 인내는 그 곳에 당신을 데려다 줄 자동차이다. -빌 브래들리-"]
mm=["성공에 대한 의지는 중요하다. 그러나 더 중요한 것은 성공을 준비하려는 의지이다. -바비 나이트-" , "자신감이 있을 때, 즐길 수 있고, 즐길 때, 당신은 놀라운 일들을 할 수 있다. -조 나마스-" , "문제는 시간이 없는 것이 아니라 방향이 없는 것이다. 우리 모두는 24시간을 가지고 있다. -지그 지글러-" , "전투 (시험) 를 준비하면서, 언제나 계획은 쓸모 없으나 꼭 필요한 것이라는 사실을 깨닫는다. -드와이트 아이젠하워-" , "아는 것으로는 충분하지 않다. 실천해야 한다. 의지만으로는 충분하지 않다. 실행해야 한다. -요한 볼프강 폰 괴테-" , "나에게 6시간을 주며 나무를 자르라고 하면, 처음 네 시간은 도끼를 가는데 쓸 것이다. -아브라함 링컨-"]
mmm=["성공은 노력에 달려 있다. -소포클레스-", "우표를 생각해보라. 그것의 유용성은 어딘가에 도달할 때까지 어떤 한 가지에 들러붙어 있는 데 있다. -조시 빌링스-" , "크게 울부짖는 것만이 용기가 아니다.'내일 다시 해보자'라고 말하는 작은 목소리도 용기이다. -메리 앤 라드마커-" , "남들보다 잘하려고 하지 말고 지금의 나보다 잘 하려고 하라. -윌리엄 포크너-" , "성공이라는 못을 박으려면 끈질김이란 망치가 필요하다. -존 메이슨-"]
for i in mm:
    m.append(i)
for i in mmm:
    m.append(i)
ment = random.choice(m) # 랜덤 격언



# 현재 날짜
now_date  = datetime.now().date()

def suntek():
    print("( 1. 전혀 아니다 / 2. 아니다 / 3. 보통이다 / 4. 그렇다 / 5. 매우 그렇다 )")

def test():
    sum=0
    print()
    print("1. 시험지를 받고 문제를 훑어볼 때 나도 모르게 걱정이 앞선다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("2. 시험공부가 잘 안 될 때 짜증만 난다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("3. 시험 문제의 답이 알쏭달쏭하고 생각나지 않을 때 시험 준비를 더 열심히 하지 않은 것을 후회한다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("4. 부모님이 시험이나 성적에 관해 물어보실 때 겁을 먹고 어찌할 바를 모른다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("5. 친구들과 답을 맞춰보면서 시험에 대해 얘기를 나눌 때 나보다 친구들이 더 좋은 점수를 받았다는 생각에 시달린다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("6. 시험 치기 직전 책이나 참고서를 봐도 머리에 잘 들어오지 않는다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("7. 시험지를 받을 때 가슴이 두근거릴 정도로 긴장한다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("8. 답안지를 제출할 때 혹시 표기를 잘못하지 않았는지 신경이 쓰인다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("9. 시험 치기 전날 신경이 날카로워져 소화가 잘 안 된다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("10. 답안지에 답을 적는 순간에도 손발이 떨린다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("11. 시험 문제를 푸는 중에도 잘못 답하지 않았는지 걱정하며 애를 태운다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("12. 시험을 치다가 시간이 부족하다는 것을 느꼈을 때 허둥대고 당황한다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("13. 시험이 끝나고 집으로 돌아갈 때 힘이 빠진다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("14. 시험 문제가 어렵고 잘 풀리지 않을 때 가슴이 답답하고 입이 마른다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("15. 시험 날짜와 시간표가 발표될 때 시험 걱정 때문에 마음의 여유가 없어진다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("16. 시험공부를 다 하지 못하고 잠이 들었다 깼을 때 눈앞이 캄캄하고 막막하다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("17. 틀린 답을 썼거나 표기를 잘못했을 때 가슴이 몹시 조마조마해진다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("18. 선생님이 시험 점수를 불러주실 때 불안하고 초조하다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("19. 자신이 없거나 많이 공부하지 못한 과목의 시험을 칠 때 좌절감을 느낀다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("20. 부모님께 성적표를 보여드리기가 두렵다."); suntek(); suntek_ch=int(input()); sum+=suntek_ch; print()
    print("<<<<<<<<합계는 %d 점 이에요>>>>>>>>" %sum)
    print()
    if sum <= 35: 
        print("|   시험에 큰 스트레스를 느끼지 않군요. 하지만 시험 볼 떄 약간의 긴장은 필요하답니다.")
        print("|   긴장이 풀어져 문제풀이에 집중을 못하거나 답안을 잘못 쓰지 않도록 주의하세요.")
    elif sum <= 60:
        print("|   보통 수준의 스트레스를 받고 있군요. 하지만 벼락치기 공부를 하거나 자신 없는 과목 시험을 치를 때는 평정심이 무너질 수도 있어요.")
        print("|   그러니 시험 전 학습 계획을 철저히 세우고 성실히 실행해 가세요.")
    elif sum <= 80:
        print("|   긴장과 불안 때문에 학습 효율이 떨어진 상태로군요.")
        print("|   시험 스트레스를 줄이는 데는 친구들과의 수다나 부모님과의 진솔한 대화가 약이 됩니다.")
        print("|   현재 자신이 가진 스트레스를 솔직하게 털어놓고 용기를 얻으세요.")
        print("|   이렇게 하다보면 시험 스트레스가 점차 줄어들 겁니다.")
    else:
        print("|   일상생활에서도 스트레스와 불안 정도가 높고, 시험이란 말만 들어도 온몸이 긴장할 정도입니다.")
        print("|   한시라도 빨리 상담기관이나 신경정신과 병원 등을 찾아 전문가의 도움을 받아야 합니다.")

def plan(): # 1.계획

    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│                                     │")
    print("│     계획 세우기를 선택하셨군요!     │")
    print("│       시험을 몇 일에 치시나요?      │")
    print("│                                     │")
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    print()

    # 시험 날짜 입력 받기
    print("조건에 맞게 적어주세요.")
    input_date = input("시험 날짜 (YYYY-MM-DD): ")

    # 입력 날짜를 datetime 객체로 변환
    input_date = datetime.strptime(input_date, "%Y-%m-%d").date()

    # 입력 날짜와 현재 날짜 사이의 차이 계산
    delta = input_date - now_date

    days_left = delta.days

    # 현재 날짜와 입력 날짜 비교
    if now_date < input_date: # 시험날이 현재보다 뒤일 경우

        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│        시험까지 %d일 남았네요!      │" %days_left)
        print("│              ☆٩(｡•ω<｡)و             │")
        print("│                                     │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│                시험은               │")
        print("│           몇 과목 치시나요?         │")
        print("│                                     │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        print()

        print("조건에 맞게 적어주세요.")
        subject = int(input("과목 개수 (숫자만 입력): "))
        
        if days_left >= subject: # 남은 날짜가 시험칠 과목보다 많으면

            # days_left(남은날) / subject(과목수) --> avg(한과목당 평균 공부할 날)
            avg = days_left / subject
            time.sleep(1); print()
            print("┌—————————————————————————————————————┐")
            print("│                                     │")
            print("│                                     │")
            print("│       오늘부터 한 과목당 '평균'     │")
            print("│        %d 일씩 공부하면 돼요!        │ " %avg)
            print("│                                     │")
            print("│                                     │")
            print("└—————————————————————————————————————┙")
            time.sleep(1); print()
            print("  ()♥() ()☆() ")
            print(" (*^-^) (^-^*) ")
            print(" ┏○━━━━○○━━━━○┓ ")
            print(" ┃D-%d  홧팅!!┃" %days_left)
            print(" ┗━━━━━━━━━━━━┛")
            print()
            time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료

        elif days_left < subject: # 남은 날짜가 시험칠 과목보다 적으면

            # subject(과목수) / days_left(남은날) /  --> avg(하루당 평균 공부할 과목 수)
            avg = subject / days_left
            time.sleep(1); print()
            print("┌—————————————————————————————————————┐")
            print("│                                     │")
            print("│                                     │")
            print("│            하루에 적어도            │")
            print("│       %d 과목이상 공부해야해요!      │" %avg)
            print("│                                     │")
            print("│                                     │")
            print("└—————————————————————————————————————┙")
            time.sleep(1);print()
            print("  ()♥() ()☆() ")
            print(" (*^-^) (^-^*) ")
            print(" ┏○━━━━○○━━━━○┓ ")
            print(" ┃D-%d  홧팅!!┃" %days_left)
            print(" ┗━━━━━━━━━━━━┛")
            print()
            time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료

    elif now_date > input_date: # 시험날이 현재보다 앞일 경우

        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│         날짜가 이미 지났네요        │")
        print("│           ヽ（゜ロ゜；）ノ          │")
        print("│                                     │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료

    else: # 시험날이 현재일 경우

        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│        오늘이네요!!! 화이팅!!       │")
        print("│            ヾ(๑ㆁᗜㆁ๑)ﾉ”            │")
        print("│                                     │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        time.sleep(1); print("*  *  *")
        print("--종료--")
        exit() # 종료

def lucky(): # 2.럭키

    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│                                     │")
    print("│        lucky를 선택하셨군요!        │")
    print("│       무엇을 알고 싶으신가요?       │")
    print("│                                     │")
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    print()

    lucky_Choice = int(input("( 1. 행운의 색 / 2. 행운의 번호 )"))
    
    if lucky_Choice == 1: # 색을 선택한 경우

        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│             오늘 당신의             │")
        print("│            **  LUCKY  **            │")
        print("│            **  COLOR  **            │")
        print("│             알려드릴게요!           │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        for i in range(1,4): 
            time.sleep(1); print("*   %d   *" %i)
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│             행운의 색깔은           │")
        print("│          바로 %s 입니다!        │" %color)
        print("│                                     │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        time.sleep(1); print()
        print(" ┃┃┃ 여기!포크에요 ")
        print(" ┣╋┫ 시험공부잘 ")
        print(" ┗╋┛ 하구이걸로 ")
        print("  ┃  정답잘찍어요! ")
        print("  ┃  ^_^")
        print()
        time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료

    elif lucky_Choice == 2: # 번호를 선택한 경우

        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│             오늘 당신의             │")
        print("│            **  LUCKY  **            │")
        print("│            **  NUMBER  **           │")
        print("│             알려드릴게요!           │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        for i in range(1,4):
            time.sleep(1); print("*   %d   *" %i)
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│             행운의 번호는           │")
        print("│           바로 %d 번 입니다!         │" %number)
        print("│                                     │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        time.sleep(1); print()
        print(" ┃┃┃ 여기! 포크에요 ")
        print(" ┣╋┫ 시험공부잘 ")
        print(" ┗╋┛ 하구이걸로 ")
        print("  ┃  정답잘찍어요! ")
        print("  ┃  ^_^")
        print()
        time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료

def maxim(): # 3.격언
    
    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│         격언을 선택하셨군요!        │")
    print("│      제가 당신께 도움이 될만한      │")
    print("│             도움이 될만한           │")
    print("│        격언을 알려드릴게요.         │")
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    print()

    print("【",ment," 】"); print()
    time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료
    

def health(): # 4.건강

    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│                                     │")
    print("│         건강을 선택하셨군요!        │")
    print("│       무엇을 알고 싶으신가요?       │")
    print("│                                     │")
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    print()

    health_Choice = int(input("( 1. 긴장 / 2. 스트레스 / 3. 상담 )"))

    if health_Choice==1: 
        print()
        print("1) 복식호흡하기"); hc1 = input("( 자세히 알아보길 원하면 '!'입력 아니면 엔터) : ")
        if hc1=='!':
            print()
            print(" ① 편한 곳에 앉아 배가 공기로 불룩해진다고 상상하며 천천히 숨을 들이쉰다.")
            print(" ② 다시 배에 있는 공기를 전부 내뱉는다고 생각하고 천천히 내쉰다.")
            print(" ③ 몸이 이완될 때까지 약 5~10분 동안 반복한다. 하루에 2, 3번 하면 좋다.")
        print()
        print("2) 과호흡이 온 경우"); hc2 = input("( 자세히 알아보길 원하면 '!'입력  아니면 엔터) : ")
        if hc2=='!':
            print()
            print(" ① 숨을 천천히 들이쉰다.")
            print(" ② 들이 쉰 상태에서 멈추지 말고 연이어 천천히 내쉰다.")
            print(" ③ 숨을 다 내 쉰 상태에서 6~10초간 잠시 멈췄다가 다시 숨을 들이쉰다.")
            print(" ④ 위와 같이 2~3분 반복한다.")
        print()
        print("3) 점진적 근육 이완법"); hc3 = input("( 자세히 알아보길 원하면 '!'입력  아니면 엔터) : ")
        if hc3=='!':
            print()
            print(" ① 승모근에 힘을 주고 5초 버텼다가 10초간 다시 근육을 이완시킨다.")
            print(" ② 누운 자세에서 손부터 시작해 팔, 어깨, 목, 미간 등 순서를 변경해 가며 천천히 연습해 본다")
            print(" ③ 복식호흡과 병행하면 효과가 더 좋다.")
        print()
        print("4) 딴짓도 제대로 하면 도움 된다"); hc4= input("( 자세히 알아보길 원하면 '!'입력  아니면 엔터) : ")
        if hc4=='!':
            print()
            print("|   단순하지만 반복적인 활동을 천천히 해보는 것도 마음을 다스리는 데 도움이 된다.")
            print("|   본인에게 맞는 것을 택해 평소 하던 것보다 속도를 '천천히' 한다.")
            print("|   반면 빠르게 다리를 떨거나 강박적으로 손톱을 물어뜯는 행동은 오히려 불안감을 증폭시킬 수 있는 행동이다.")
        print()
        print("5) 걱정거리에 대해 글을 쓰는 것"); hc5= input("( 자세히 알아보길 원하면 '!'입력  아니면 엔터) : ")
        if hc5=='!':
            print()
            print("|   감정을 정리하는 글쓰기 행위는 일종의 카타르시스를 일으키게 되고, 결과적으로 마음을 비우고 집중하는 데 도움이 된다.")
        print()
        print("+ 약 복용X"); hc6= input("( 자세히 알아보길 원하면 '!'입력  아니면 엔터) : ")
        if hc6=='!':
            print()
            print("|   긴장은 낮아질 수 있겠지만, 정작 인지기능이 떨어질 수도 있다.")
            print("|   약물에 의지하기 보다는 시험 며칠 전부터 규칙적인 수면과 식사를 하면서 컨디션을 유지하는 것이 최선법이다.")
        time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료
        
    elif health_Choice==2: 
        print()
        print("1) 충분한 휴식과 운동하기")
        print("2) 카페인 피하기, 가공식품 멀리하기, 균형있는 식사하기")
        print("3) 에센셜 오일 사용 - 라벤더(불면증 완화), 네롤리(불안 완화), 일랑일랑(자존감 향상), 페퍼민트(메스꺼움, 두통 완화) 등")
        time.sleep(1); print()
        print("┌—————————————————————————————————————┐")
        print("│                                     │")
        print("│                                     │")
        print("│      스트레스 지수를 알아볼 수      │")
        print("│       있는 검사를 원하시나요??      │")
        print("│               (20문항)              │")
        print("│                                     │")
        print("└—————————————————————————————————————┙")
        print("*출처: <한국형 시험불안 척도(K-TAI-K)>, 황경렬 《한국심리학회지》"); print()
        st_Choice = int(input("( 1. 네 / 2. 아니오 )"))
        if st_Choice==1: 
            test()
            time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료
        else:
            time.sleep(1); print()
            print("┌—————————————————————————————————————┐")
            print("│                                     │")
            print("│                                     │")
            print("│              알겠습니다             │")
            print("│               ヾ(°∇°*)              │")
            print("│                                     │")
            print("│                                     │")
            print("└—————————————————————————————————————┙")
            time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료
    
    elif health_Choice==3: 
        print()
        print("|  전화상담 유선전화 국번없이 '1388'")
        print("|  휴대전화 '031-1388'")
        print("|  사이버상담 'www.cyber1388.kr' 접속 후 채팅 및 게시판 상담")
        print("|  문자상담 '#1388'로 상담내용 문자전송")
        print("|  카카오톡 상담 플러스 친구에서 '#1388' 친구 맺기 후 상담")
        print()
        time.sleep(1); print("*  *  *"); print("--종료--"); exit() #종료

def tip(): # 5.팁
    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│                                     │")
    print("│        공부팁을 선택하셨군요!       │")
    print("│         교육부에서 알려주는         │")
    print("│        방법을 소개해드릴게요.       │")
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    time.sleep(1); print()
    print("1) 수업시간에 집중하기")
    print("|   수업시간의 태도가 자신의 시험점수를 좌우한다고 생각하고 수업시간에 꼭 집중하세요."); time.sleep(1); print()
    print("2) 계획 세우기와 시간관리")
    print("|   계획을 세우지 않을 때보다 훨씬 많은 시간을 유용하게 사용할 수 있고, 계획 실천 여부를 확인하면서 스스로 반성하고 더 개선해 나아갈 수 있는 계기가 될 수 있습니다."); time.sleep(1); print()
    print("3) 교과서 반복 복습")
    print("|   모든 문제는 거의 모두 교과서에서 나오기 때문입니다. 문제집을 푸는 것도 중요하지만, 우선 교과서를 계속 읽으세요.(7번 정도)"); time.sleep(1); print()
    print("4) 노트 정리")
    print("|    그래프나 그림 같은 경우에는 직접 그려서 한눈에 보기 쉽게 하고, 필기는 시험시간 바로 전에 볼 수 있도록 간략하고 명료하게 정리하면 좋습니다. "); time.sleep(1); print()
    print("5) 컨디션 조절")
    print("|   시험기간에는 계획에 맞춰 공부하고 꼭 자신이 정한 시간 내에 잠드세요."); time.sleep(1); print()
    print("6) 끝까지 열심히")
    print("|   당일 본 시험의 결과를 생각하지 말고 내일 볼 시험을 위해 열심히 공부하세요."); print()
    print("  ☆ハ  バ ")
    print(" ☆ミⓛㅅⓛミ ")
    print(" ┏━o━━━o━━━━━━┓ ")
    print(" ┃시험잘보세요┃ ")
    print(" ┗━━━━━━━━━━━━┛")
    print(); time.sleep(1); print("*  *  *"); print("--종료--"); exit() # 종료
#start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print("┌—————————————————————————————————————┐")
print("│                                     │")
print("│                                     │")
print("│       안녕하세요 저는 시우에요      │")
print("│      저의 도움이 필요하신가요?      │")
print("│                                     │")
print("│                                     │")
print("└—————————————————————————————————————┙")
time.sleep(1); print()
print("(해당 숫자만 입력)")
start=input("( 1. 네 / 2. 아니오 )")

if start=='2':

    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│                                     │")
    print("│              알겠습니다             │")
    print("│              (´；Д；｀)             │")
    print("│                                     │")
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    time.sleep(1); print("*  *  *")
    print("--종료--")
    exit() # 종료

elif start=='1':

    time.sleep(1); print()
    print("┌—————————————————————————————————————┐")
    print("│                                     │")
    print("│          저는 시험에 관련된         │")
    print("│      다양한 일을 도와준답니다.      │")
    print("│       당신이 필요로 하는 것을       │")
    print("│             선택하세요!             │")    
    print("│                                     │")
    print("└—————————————————————————————————————┙")
    time.sleep(1); print()
    choice=input("( 1. 계획세우기 / 2. lucky / 3. 격언 / 4. 건강 / 5. 공부팁 )")

    if choice=='1': plan()
    elif choice=='2': lucky()
    elif choice=='3': maxim()
    elif choice=='4': health()
    elif choice=='5': tip()