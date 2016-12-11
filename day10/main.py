import re
from Bot import Bot
from Output import Output

BOT_RE = re.compile(r"value\s(\d+)\sgoes\sto\sbot\s(\d+)")
HILOW_RE = re.compile(r"bot\s(\d+)\sgives\slow\sto\s([a-z]{3,6})\s(\d+)\sand\shigh\sto\s([a-z]{3,6})\s(\d+)")

bots = dict()
outputs = dict()

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.read().splitlines()

def exec_instructions(insts):
    while insts:
        for inst in insts:
            done = False
            if BOT_RE.match(inst):
                done = init_bot(inst)
            else:
                done = pass_value(inst)

            if done:
                insts.remove(inst)

def init_bot(inst):
    for value, bot_nr in BOT_RE.findall(inst):
        bot_nr = int(bot_nr)
        value = int(value)

        if bot_nr in bots:
            bots[bot_nr].add_value(value)
        else:
            bots[bot_nr] = Bot(bot_nr, value)
    return True

def pass_value(inst):
    for bot_nr, rec_low, rec_low_nr, rec_hi, rec_hi_nr in HILOW_RE.findall(inst):
        bot_nr = int(bot_nr)
        rec_low_nr = int(rec_low_nr)
        rec_hi_nr = int(rec_hi_nr)

        bot = get_bot(bot_nr)
        if not bot.is_ready():
            return False

        receiver_low = get_output(rec_low_nr) if rec_low == "output" else get_bot(rec_low_nr)
        receiver_hi = get_output(rec_hi_nr) if rec_hi == "output" else get_bot(rec_hi_nr)

        bot.give_low(receiver_low)
        bot.give_hi(receiver_hi)

    return True

def get_output(num):
    if num not in outputs:
        outputs[num] = Output(num, None)
    return outputs[num]

def get_bot(num):
    if num not in bots:
        bots[num] = Bot(num, None)
    return bots[num]

def main():
    exec_instructions(get_file())
    result = [bot for k, bot in bots.items() if (61, 17) in bot.values_compared]
    print(result)

    # part 2
    result2 = outputs[0].value * outputs[1].value * outputs[2].value
    print(result2)

if  __name__ == '__main__': main()
# 157
# part 2
# 1085
