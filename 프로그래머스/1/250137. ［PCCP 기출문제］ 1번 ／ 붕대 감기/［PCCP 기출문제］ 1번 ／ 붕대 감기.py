def solution(bandage, health, attacks):
    hp = 0
    skill, hill, hill_plus = bandage
    final_time = attacks[-1][0]
    count = 0
    skill_success = 0
    hp = health

    for time in range(final_time+1):
        attack_time, damage = attacks[count]
        if time == attack_time:
            hp -= damage
            skill_success = 0
            count += 1
            if hp <= 0 or count>len(attacks): 
                break
        
        elif hp < health:
            hp += hill
            skill_success += 1
            if skill_success == skill:
                hp += hill_plus
                skill_success = 0
            if hp > health: hp = health
    hp = -1 if hp <= 0 else hp
    
    return hp