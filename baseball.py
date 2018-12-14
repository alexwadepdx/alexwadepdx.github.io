#lets play Baseball!!!!!!
import random
import time



def call_pitch():
    pitch = random.randint(1, 20)
    time.sleep(3)
    if pitch < 5:
        pitch = "ball"
        return(pitch)
    
    if pitch == 5 or pitch == 11:
        pitch = "It's a Hit!"
        return(pitch)
            
    if pitch > 5 and pitch < 11:
        pitch = "strike"
        return(pitch)

    if pitch > 11 and pitch < 16:
        pitch = "Ground out"
        return(pitch)

    if pitch > 15:
        pitch = "Fly out"
        return(pitch)


def plate_appearance():
    hidden_outs = 0
    outs = 0
    balls = 0
    strikes = 0
    innings = 1
    home_score = 0
    away_score = 0
    first_base = 0
    second_base = 0
    third_base = 0
    home_team = input("enter name of home team ")
    away_team = input("enter name of away team ")
    print(f'the score is {home_team} 0 - {away_team} 0')
    print("Play Ball!")
    if innings <= 9:
        while hidden_outs <= 6:
            if hidden_outs == 6:
                innings += 1
                if innings == 1:
                    show_innings = str(innings) + "st"
                elif innings == 2:
                    show_innings = str(innings) + "nd"
                elif innings == 3:
                    show_innings = str(innings) + "rd"
                else:
                    show_innings = str(innings) + "th"
                print (show_innings)
                print (f'{away_team} - {away_score}')
                print (f'{home_team} - {home_score}')
                hidden_outs = 0
            pitch = call_pitch()
            print(pitch)
            if pitch == "ball":
                balls +=1
                if balls == 4:
                    print("batter walks")
                    balls = 0
                    strikes = 0
                    first_base += 1
                    if first_base > 1:
                        second_base += 1
                        if second_base > 1:
                            third_base += 1
                            if third_base > 1:
                                if hidden_outs <= 2:
                                    away_score += 1
                                elif hidden_outs > 2:
                                    home_score += 1

                    
            if pitch == "strike":
                strikes +=1
                if strikes == 3:
                    outs += 1
                    hidden_outs += 1
                    strikes = 0
                    balls = 0
                    print("Strike three, batter's out!")
                    print(f'{outs} down')
                    if outs > 2:
                        print("switch sides")
                        outs = 0
                        first_base = 0
                        second_base = 0
                        third_base = 0
                            
            if pitch == "Ground out":
                strikes = 0
                balls = 0
                outs += 1
                hidden_outs += 1
                print(f'{outs} down')
                if outs > 2:
                        print("switch sides")
                        outs = 0
                        first_base = 0
                        second_base = 0
                        third_base = 0

            if pitch == "Fly out":
                strikes = 0
                balls = 0
                outs += 1
                hidden_outs += 1
                print(f'{outs} down')
                if outs > 2:
                        print("switch sides")
                        outs = 0
                        first_base = 0
                        second_base = 0
                        third_base = 0


            if pitch == "It's a Hit!":
                balls = 0
                strikes = 0
                hit_list = ["Single", "Double", "Triple", "HomeRun"]
                bases = random.randint(1, 10)
                if bases <= 6:
                    hit = hit_list[0]
                    first_base += 1
                    if first_base > 1:
                        second_base += 1
                        first_base = 1
                        if second_base > 1:
                            if hidden_outs <= 2:
                                away_score += 1
                            elif hidden_outs > 2:
                                home_score += 1
                            second_base = 1
                    if third_base == 1:
                        if hidden_outs <= 2:
                            away_score += 1
                        elif hidden_outs > 2:
                            home_score += 1
                        third_base = 0
                if bases == 7 or bases == 8:
                    hit = hit_list[1]
                    second_base += 1
                    if second_base > 1:
                        if hidden_outs <= 2:
                            away_score += 1
                        elif hidden_outs > 2:
                            home_score += 1
                        second_base = 1
                    if first_base == 1:
                        third_base += 1
                        first_base = 0
                    if third_base == 1:
                        if hidden_outs <= 2:
                            away_score += 1
                        elif hidden_outs > 2:
                            home_score += 1
                        third_base = 0
                if bases == 9:
                    hit = hit_list[2]
                    third_base += 1
                    if third_base > 1:
                        if hidden_outs < 3:
                            away_score += 1
                        if hidden_outs > 2:
                            home_score += 1
                    if first_base == 1:
                        if hidden_outs < 3:
                            away_score += 1
                        if hidden_outs > 2:
                            home_score += 1
                        first_base = 0
                    if second_base == 1:
                        if hidden_outs < 3:
                            away_score += 1
                        if hidden_outs > 2:
                            home_score += 1
                        second_base = 0
                    third_base = 1
                if bases == 10:
                    hit = hit_list[3]
                    if hidden_outs < 3:
                        away_score += 1
                    if hidden_outs > 2:
                        home_score += 1
                    if first_base == 1:
                        if hidden_outs < 3:
                            away_score += 1
                        if hidden_outs > 2:
                            home_score += 1
                    if second_base == 1:
                        if hidden_outs < 3:
                            away_score += 1
                        if hidden_outs > 2:
                            home_score += 1
                    if third_base == 1:
                        if hidden_outs < 3:
                            away_score += 1
                        if hidden_outs > 2:
                            home_score += 1
                    first_base = 0
                    second_base = 0
                    third_base = 0
                print(hit)

                
                    

########## you need to fix innings, they are not incrementing, game in running beyon 9 innings########
    

def game():
    print("Let's play Baseball!!!")
    time.sleep(3)
    plate_appearance()
    

game()

        
        

        
