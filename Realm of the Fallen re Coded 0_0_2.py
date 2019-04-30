#Realm of the Fallen re:Coded;
#Libraries;
import time;
import os;
import platform;

#Variables;
username = 'NULL';
password = 'NULL';

#Bank Accounts/Money
money = 500;
bankAccount1Gold = 0;
bankAccount1Message = 'Open';
bankAccount2Gold = 0;
bankAccount2Message = 'Open';
bankAccount3Gold = 0;
bankAccount3Message = 'Open';
bankAccount4Gold = 0;
bankAccount4Message = 'Open';
bankAccount5Gold = 0;
bankAccount5Message = 'Open';
bankgold = 0;
bankchoice = 0;

#Shop Storage
itemCost = 0;
storeChoice = 0;

#Player Statss
currentLevel = 1;
HP = 200;
maxHP = 200;

#Monster Status
dmgnpc = 0;
killcount = 0;

playerxp = 0;
xpuntil = 500;
origxp = 500;

key = 0;
damage = 0;
dr =  0;

#Amount of Materials
goblinMail = 0;
hugeBone = 0;
dragonHide = 0;
runicTablet = 0;
potion = 0;
food = 0;
seed = 0;
fur = 0;
ore = 0;
log = 0;
gemstone = 0;
magicOrb = 0;
rawFood = 0;
bait = 0;
ingot = 0;
bow = 0;

#Price of items TBD
priceGoblinMail = 300;
priceHugeBone = 550;
priceDragonHide = 750;
priceRunicTablet = 250;
pricePotion = 200;
priceFood = 100;
priceSeed = 150;
priceFur = 200;
priceOre = 500;
priceLog = 275;
priceGemstone = 1000;
priceMagicOrb = 15000;
priceRawFood = 100;
priceBait = 2;
priceIngot = 473;
priceBow = 713;

#Amount of Armor
clothArmor = 0;
chainArmor = 0;
ironArmor = 0;
steelArmor = 0;
crystalArmor = 0;
sacredArmor = 0;
infernalArmor = 0;

#Amount of Swords
woodenSword = 0;
stoneSword = 0;
ironSword = 0;
steelSword = 0;
crystalSword = 0;
sacredBlade = 0;
infernalRapier = 0;
omegaMaul = 0;
mythicalGodsword = 0;

#Woodcutting Stats
Woodcuttinglvl = 1;
Woodcuttingxpremain = 100;
Woodcuttingxpgain = 38;
Woodcuttingcurxp = 0;
Woodcuttingxpleft = 100;

#Cooking Stats
Cooklvl = 1;
Cookxpremain = 100;
Cookxpgain = 41;
Cookcurxp = 0;
Cookxpleft = 100;

#Fishin Stats
Fishinglvl = 1;
Fishingxpremain = 100;
Fishingxpgain = 30;
Fishingcurxp = 0;
Fishingxpleft = 100;

#Mining Stats
Mininglvl = 1;
Miningxpremain = 100;
Miningxpgain = 35;
Miningcurxp = 0;
Miningxpleft = 100;

#Smithing Stats
Smithinglvl = 1;
Smithingxpremain = 100;
Smithingxpgain = 33;
Smithingcurxp = 0;
Smithingxpleft = 100;

#Thieving Stats
Thievinglvl = 1;
Thievingxpremain = 100;
Thievingxpgain = 36;
Thievingcurxp = 0;
Thievingxpleft = 100;
ttllvl = 13;

#Boot Screen;
def entergame():
    os.system('cls');
    print('What would you like to do?');
    print();
    print('1) Create Account');
    print('2) Login');
    print('4) Exit');
    print();
    print();
    print('Current Version: v0.01alpha');
    try:
        x = int(input());
        if x == 1:
            createuser();
        elif x == 2:
            login();
        elif x == 3:
            print('Null');
            entergame();
        elif x == 4:
            os.system('cls');
            exit();
        else:
            entergame();
    except ValueError:
        entergame();
#Username Create;
def createuser():
    global username;
    os.system('cls');
    print('What would you like you username to be?');
    username = str(input());
    checkforspaces()
#Checks Username For Spaces;
def checkforspaces():
    global password;
    if ' ' in username:
        print("Sorry, you can't use spaces in your username.");
        time.sleep(1.5);
        createuser();
#Creates Password;
    else:
        print();
        print('What would you like your password to be?');
        password = str(input());
        DATA_VALUES();
#Login Work on later;
def login():
    os.system('cls');
#Creates Save;
def DATA_VALUES():
    global bankAccount1Gold;
    global bankAccount1Message;
    global bankAccount2Gold;
    global bankAccount2Message;
    global bankAccount3Gold;
    global bankAccount3Message;
    global bankAccount4Gold;
    global bankAccount4Message;
    global bankAccount5Gold;
    global bankAccount5Message;
    global cost;
    global cost1;
    global gcho;
    global dmgnpc;
    global ls1;
    global killcount;
    global ls2;
    global la1;
    global la2;
    global HP;
    global maxHP;
    global armtype;
    global swordtype;
    global skind;
    global buyword1;
    global buyword2;
    global currentLevel;
    global aan;
    global bankchoice;
    global bankgold;
    global swordchoice;
    global swordchoice2;
    global swordchoice3;
    global swordexist;
    global sprice;
    global armchoice;
    global armchoice;
    global aprice;
    global playerxp;
    global xpuntil;
    global origxp;
    global money;
    global key;
    global damage;
    global dr;
    global goblinMail;
    global hugeBone;
    global dragonHide;
    global runicTablet;
    global food;
    global rawFood;
    global bait;
    global ea;
    global potion;
    global ingot;
    global seed;
    global bow;
    global fur;
    global gemstone;
    global log;
    global ore;
    global magicOrb;
    global clothArmor;
    global chainArmor;
    global ironArmor;
    global steelArmor;
    global crystalArmor;
    global sacredArmor;
    global infernalArmor;
    global arm8;
    global arm9;
    global arm10;
    global arm11;
    global arm12;
    global ma1;
    global ma2;
    global ma3;
    global ma4;
    global ma5;
    global ma6;
    global ma7;
    global ma8;
    global ma9;
    global ma10;
    global ms1;
    global ms2;
    global ms3;
    global ms4;
    global ms5;
    global ms6;
    global ms7;
    global ms8;
    global ms9;
    global ms10;
    global woodenSword;
    global stoneSword;
    global ironSword;
    global steelSword;
    global crystalSword;
    global sacredBlade;
    global infernalRapier;
    global omegaMaul;
    global mythicalGodsword;
    global sword10;
    global sword11;
    global sword12;
    global axxx;
    global priceGoblinMail;
    global priceHugeBone;
    global priceDragonHide;
    global priceRunicTablet;
    global pricePotion;
    global priceFood;
    global priceIngot;
    global priceSeed;
    global priceRawFood;
    global priceBait;
    global priceFur;
    global priceOre;
    global priceLog;
    global priceGemstone;
    global priceBow;
    global priceMagicOrb;
    global Woodcuttinglvl;
    global Woodcuttingxpremain;
    global Woodcuttingxpgain;
    global Woodcuttingcurxp;
    global Woodcuttingxpleft;
    global Cooklvl;
    global Cookxpremain;
    global Cookxpgain;
    global Cookcurxp;
    global Cookxpleft;
    global Fishinglvl;
    global Fishingxpremain;
    global Fishingxpgain;
    global Fishingcurxp;
    global Fishingxpleft;
    global Mininglvl;
    global Miningxpremain;
    global Miningxpgain;
    global Miningcurxp;
    global Miningxpleft;
    global Smithinglvl;
    global Smithingxpremain;
    global Smithingxpgain;
    global Smithingcurxp;
    global Smithingxpleft;
    global Thievinglvl;
    global Thievingxpremain;
    global Thievingxpgain;
    global Thievingcurxp;
    global Thievingxpleft;
    global ttllvl;
    bankAccount1Gold = 0;
    bankAccount1Message = 'Open';
    bankAccount2Gold = 0;
    bankAccount2Message = 'Open';
    bankAccount3Gold = 0;
    bankAccount3Message = 'Open';
    bankAccount4Gold = 0;
    bankAccount4Message = 'Open';
    bankAccount5Gold = 0;
    bankAccount5Message = 'Open';
    cost = '--';
    cost1 = '--';
    gcho = '--';
    echo = '--';
    e2cho = '--';
    e1 = '--';
    dmgnpc = 0;
    ls1 = 0;
    killcount = 0;
    ls2 = 0;
    la1 = 0;
    la2 = 0;
    HP = 200;
    maxHP = 200;
    armtype = 'No';
    swordtype = 'Your';
    skind = 'hand';
    buyword1 = 'hi';
    buyword2 = 'hi';
    currentLevel = 1;
    aan = 'a';
    bankchoice = 0;
    bankgold = 0;
    swordchoice = 'hi';
    swordchoice2 = 'hi';
    swordchoice3 = 'hi';
    swordexist = 'hi';
    sprice = 0;
    armchoice = 'hi';
    armchoice2 = 'Armor';
    aprice = 0;
    playerxp = 0;
    xpuntil = 500;
    origxp = 500;
    money = 500;
    key = 0;
    damage = 0;
    dr =  0;
    goblinMail = 0;
    hugeBone = 0;
    dragonHide = 0;
    runicTablet = 0;
    food = 0;
    rawFood = 0;
    bait = 0;
    potion = 0;
    ingot = 0;
    seed = 0;
    bow = 0;
    fur = 0;
    gemstone = 0;
    log = 0;
    ore = 0;
    magicOrb = 0;
    clothArmor = 0;
    chainArmor = 0;
    ironArmor = 0;
    steelArmor = 0;
    crystalArmor = 0;
    sacredArmor = 0;
    infernalArmor = 0;
    arm8 = 0;
    arm9 = 0;
    arm10 = 0;
    arm11 = 0;
    arm12 = 0;
    ma1 = 0;
    ma2 = 0;
    ma3 = 0;
    ma4 = 0;
    ma5 = 0;
    ma6 = 0;
    ma7 = 0;
    ma8 = 0;
    ma9 = 0;
    ma10 = 0;
    ms1 = 0;
    ms2 = 0;
    ms3 = 0;
    ms4 = 0;
    ms5 = 0;
    ms6 = 0;
    ms7 = 0;
    ms8 = 0;
    ms9 = 0;
    ms10 = 0;
    woodenSword = 0;
    stoneSword = 0;
    ironSword = 0;
    steelSword = 0;
    crystalSword = 0;
    sacredBlade = 0;
    infernalRapier = 0;
    omegaMaul = 0;
    mythicalGodsword = 0;
    sword10 = 0;
    sword11 = 0;
    sword12 = 0;
    axxx = 0;
    priceGoblinMail = 300;
    priceHugeBone = 550;
    priceDragonHide = 750;
    priceRunicTablet = 250;
    pricePotion = 200;
    priceFood = 100;
    priceIngot = 473;
    priceSeed = 150;
    priceRawFood = 100;
    priceBait = 2;
    priceFur = 200;
    priceOre = 500;
    priceLog = 275;
    priceGemstone = 1000;
    priceBow = 713;
    priceMagicOrb = 15000;
    Woodcuttinglvl = 1;
    Woodcuttingxpremain = 100;
    Woodcuttingxpgain = 38;
    Woodcuttingcurxp = 0;
    Woodcuttingxpleft = 100;
    Cooklvl = 1;
    Cookxpremain = 100;
    Cookxpgain = 41;
    Cookcurxp = 0;
    Cookxpleft = 100;
    Fishinglvl = 1;
    Fishingxpremain = 100;
    Fishingxpgain = 30;
    Fishingcurxp = 0;
    Fishingxpleft = 100;
    Mininglvl = 1;
    Miningxpremain = 100;
    Miningxpgain = 35;
    Miningcurxp = 0;
    Miningxpleft = 100;
    Smithinglvl = 1;
    Smithingxpremain = 100;
    Smithingxpgain = 33;
    Smithingcurxp = 0;
    Smithingxpleft = 100;
    Thievinglvl = 1;
    Thievingxpremain = 100;
    Thievingxpgain = 36;
    Thievingcurxp = 0;
    Thievingxpleft = 100;
    ttllvl = 13;
    SAVE_GAME_FILES();
#Main Menu
def MENU():
    global ttllvl;
    ttllvl = Woodcuttinglvl + Cooklvl + Fishinglvl +Mininglvl + Smithinglvl+ Thievinglvl;
    os.system('cls');
    print('***************************');
    print('*What would you like to do?*');
    print('***************************');
    print('* 1) Wander Gielinor       *');
    print('*                          *');
    print('* 2) Weapon Shop           *');
    print('*                          *');
    print('* 3) Armor Shop            *');
    print('*                          *');
    print('* 4) Legends Store         *');
    print('*                          *');
    print('* 5) Trading Post          *');
    print('*                          *');
    print('* 6) Smuggler              *');
    print('*                          *');
    print('* 7) The Stronghold        *');
    print('*                          *');
    print('* 8) Skill Plot            *');
    print('*                          *');
    print('* 9) RealmBank             *');
    print('*                          *');
    print('*97) Your Inventory        *');
    print('***************************');
    print();
    print();
    print('****************************************');
    print('   Currently logged in as',username);
    print('****************************************');
    print('*98) Settings                          *');
    print('*99) Log out                           *');
    print('****************************************');
    try:
        x1 = int(input());
        if x1 == 1:
            picknpc();
        elif x1 == 2:
            weaponstore();
        elif x1 == 3:
            Armorstore();
        elif x1 == 4:
            legendstore();
        elif x1 == 5:
            gstore();
        elif x1 == 6:
            smuggler();
        elif x1 == 7:
            STR_PIC();
        elif x1 == 8:
            skillplot();
        elif x1 == 9:
            BANK();
        elif x1 == 97:
            checkitems();
        elif x1 == 98:
            settings();
        elif x1 == 99:
            entergame();
        else:
            MENU();
    except ValueError:
        MENU();
#Sleep Time
def REST():
    global HP
    os.system('cls');
    HP = maxHP;
    print('You are now at full health and well rested!');
    time.sleep(1.5);
    MENU()
#Bank to store gold
def BANK():
    global bankchoice
    global bankgold
    os.system('cls')
    print("Welcome to RealmBank!");
    print("Here are your accounts which you can store up to 1,000,000,000 (1B) gold into each.");
    print();
    print('*******************************');
    print(' You have',money,'gold.');
    print('*******************************');
    print('      Account 1:',bankAccount1Message);
    print('         - Gold:',bankAccount1Gold);
    print();
    print('      Account 2:',bankAccount2Message);
    print('         - Gold:',bankAccount2Gold);
    print();
    print('      Account 3:',bankAccount3Message);
    print('         - Gold:',bankAccount3Gold);
    print();
    print('      Account 4:',bankAccount4Message);
    print('         - Gold:',bankAccount4Gold);
    print();
    print('      Account 5:',bankAccount5Message);
    print('         - Gold:',bankAccount5Gold);
    print('*******************************');
    print();
    print('Type "0" to exit.');
    a5 = int(input('Access account number: '));
    if a5 == int(1):
        bankchoice = str('bankAccount1Gold');
        bankgold = bankAccount1Gold;
        type (a5);
        depositwithdraw();
    elif a5 == int(2):
        bankchoice = str('bankAccount2Gold');
        bankgold = bankAccount2Gold;
        depositwithdraw();
    elif a5 == int(3):
        bankchoice = str('bankAccount3Gold');
        bankgold = bankAccount3Gold;
        depositwithdraw();
    elif a5 == int(4):
        bankchoice = str('bankAccount4Gold');
        bankgold = bankAccount4Gold;
        depositwithdraw();
    elif a5 == int(5):
        bankchoice = str('bankAccount5Gold');
        bankgold = bankAccount5Gold;
        depositwithdraw();
    elif a5 == int(0):
        SAVE_GAME_FILES();
    else:
        BANK();

def depositwithdraw():
    print();
    a8 = str(input('Deposit or withdraw? [d/w]:',));
    a8 = a8.lower();
    if a8 == str('d'):
        depositgoldintobank();
    if a8 == str('w'):
        withdrawgoldfrombank();

def depositgoldintobank():
    global bankAccount1Gold;
    global bankAccount2Gold;
    global bankAccount3Gold;
    global bankAccount4Gold;
    global bankAccount5Gold;
    global bankAccount1Message;
    global bankAccount2Message;
    global bankAccount3Message;
    global bankAccount4Message;
    global bankAccount5Message;
    global bankchoice;
    global bankgold;
    global money;
    print();
    print('How much gold would you like to deposit?');
    print('Type "all" to depost all gold');
    a6 = int(input());
    if bankchoice == str('bankAccount1Gold'):
        if int(a6) <= int(0):
            BANK();
        if int(a6) > money:
            notenoughmony();
        bankgold = bankgold + int(a6);
        bankAccount1Gold = bankgold;
        if bankgold >= 1000000000:
            money = bankgold - 1000000000 + money;
            bankgold = 1000000000;
            bankAccount1Gold = bankgold;
            bankAccount1Message = 'Closed';
            BANK();
    if bankchoice == str('bankAccount2Gold'):
        if int(a6) <= int(0):
            BANK();
        if int(a6) > money:
            notenoughmony();
        bankgold = bankgold + int(a6);
        bankAccount2Gold = bankgold;
        if bankgold >= 1000000000:
            money = bankgold - 1000000000 + money;
            bankgold = 1000000000;
            bankAccount2Gold = bankgold;
            bankAccount2Message = 'Closed';
            BANK();
    if bankchoice == str('bankAccount3Gold'):
        if int(a6) <= int(0):
            BANK();
        if int(a6) > money:
            notenoughmony();
        bankgold = bankgold + int(a6);
        bankAccount3Gold = bankgold;
        if bankgold >= 1000000000:
            money = bankgold - 1000000000 + money;
            bankgold = 1000000000;
            bankAccount3Gold = bankgold;
            bankAccount3Message = 'Closed';
            BANK();
    if bankchoice == str('bankAccount4Gold'):
        if int(a6) <= int(0):
            BANK();
        if int(a6) > money:
            notenoughmony();
        bankgold = bankgold + int(a6);
        bankAccount4Gold = bankgold;
        if bankgold >= 1000000000:
            money = bankgold - 1000000000 + money;
            bankgold = 1000000000;
            bankAccount4Gold = bankgold;
            bankAccount4Message = 'Closed';
            BANK();
    if bankchoice == str('bankAccount5Gold'):
        if int(a6) <= int(0):
            BANK();
        if int(a6) > money:
            notenoughmony();
        bankgold = bankgold + int(a6);
        bankAccount5Gold = bankgold;
        if bankgold >= 1000000000:
            money = bankgold - 1000000000 + money;
            bankgold = 1000000000;
            bankAccount5Gold = bankgold;
            bankAccount5Message = 'Closed';
            BANK();
    money = money - int(a6);
    BANK();

def withdrawgoldfrombank():
    global bankchoice
    global bankgold
    global money
    print();
    print('How much gold would you like to withdraw?');
    print('Type "all" to withdraw all gold');
    a7 = str(input());
    if int(a6) <= 0:
        BANK();
#Save System
def SAVE_GAME_FILES():
    file = open(username + '.rrcs',"w+");
    file.write(str(username) + '\n');
    file.write(str(password) + '\n');
    file.write(str(bankAccount1Gold) + '\n');
    file.write(str(bankAccount1Message) + '\n');
    file.write(str(bankAccount2Gold) + '\n');
    file.write(str(bankAccount2Message) + '\n');
    file.write(str(bankAccount3Gold) + '\n');
    file.write(str(bankAccount3Message) + '\n');
    file.write(str(bankAccount4Gold) + '\n');
    file.write(str(bankAccount4Message) + '\n');
    file.write(str(bankAccount5Gold) + '\n');
    file.write(str(bankAccount5Message) + '\n');
    file.write(str(cost1) + '\n');
    file.write(str(cost) + '\n');
    file.write(str(gcho) + '\n');
    file.write(str(dmgnpc) + '\n');
    file.write(str(ls1) + '\n');
    file.write(str(ls2) + '\n');
    file.write(str(la1) + '\n');
    file.write(str(la2) + '\n');
    file.write(str(armtype) + '\n');
    file.write(str(HP) + '\n');
    file.write(str(maxHP) + '\n');
    file.write(str(swordtype) + '\n');
    file.write(str(skind) + '\n');
    file.write(str(currentLevel) + '\n');
    file.write(str(origxp) + '\n');
    file.write(str(playerxp) + '\n');
    file.write(str(xpuntil) + '\n');
    file.write(str(swordchoice) + '\n');
    file.write(str(swordchoice2) + '\n');
    file.write(str(swordchoice3) + '\n');
    file.write(str(swordexist) + '\n');
    file.write(str(sprice) + '\n');
    file.write(str(armchoice) + '\n');
    file.write(str(armchoice2) + '\n');
    file.write(str(aprice) + '\n');
    file.write(str(money) + '\n');
    file.write(str(key) + '\n');
    file.write(str(damage) + '\n');
    file.write(str(killcount) + '\n');
    file.write(str(dr) + '\n');
    file.write(str(goblinMail) + '\n');
    file.write(str(hugeBone) + '\n');
    file.write(str(dragonHide) + '\n');
    file.write(str(runicTablet) + '\n');
    file.write(str(food) + '\n');
    file.write(str(rawFood) + '\n');
    file.write(str(potion) + '\n');
    file.write(str(bait) + '\n');
    file.write(str(seed) + '\n');
    file.write(str(fur) + '\n');
    file.write(str(gemstone) + '\n');
    file.write(str(ingot) + '\n');
    file.write(str(log) + '\n');
    file.write(str(bow) + '\n');
    file.write(str(ore) + '\n');
    file.write(str(aan) + '\n');
    file.write(str(bankchoice) + '\n');
    file.write(str(magicOrb) + '\n');
    file.write(str(clothArmor) + '\n');
    file.write(str(chainArmor) + '\n');
    file.write(str(ironArmor) + '\n');
    file.write(str(steelArmor) + '\n');
    file.write(str(crystalArmor) + '\n');
    file.write(str(sacredArmor) + '\n');
    file.write(str(infernalArmor) + '\n');
    file.write(str(arm8) + '\n');
    file.write(str(arm9) + '\n');
    file.write(str(arm10) + '\n');
    file.write(str(arm11) + '\n');
    file.write(str(arm12) + '\n');
    file.write(str(ma1) + '\n');
    file.write(str(ma2) + '\n');
    file.write(str(ma3) + '\n');
    file.write(str(ma4) + '\n');
    file.write(str(ma5) + '\n');
    file.write(str(ma6) + '\n');
    file.write(str(ma7) + '\n');
    file.write(str(ma8) + '\n');
    file.write(str(ma9) + '\n');
    file.write(str(ma10) + '\n');
    file.write(str(ms1) + '\n');
    file.write(str(ms2) + '\n');
    file.write(str(ms3) + '\n');
    file.write(str(ms4) + '\n');
    file.write(str(ms5) + '\n');
    file.write(str(ms6) + '\n');
    file.write(str(ms7) + '\n');
    file.write(str(ms8) + '\n');
    file.write(str(ms9) + '\n');
    file.write(str(ms10) + '\n');
    file.write(str(woodenSword) + '\n');
    file.write(str(stoneSword) + '\n');
    file.write(str(ironSword) + '\n');
    file.write(str(steelSword) + '\n');
    file.write(str(crystalSword) + '\n');
    file.write(str(sacredBlade) + '\n');
    file.write(str(infernalRapier) + '\n');
    file.write(str(omegaMaul) + '\n');
    file.write(str(mythicalGodsword) + '\n');
    file.write(str(sword10) + '\n');
    file.write(str(sword11) + '\n');
    file.write(str(sword12) + '\n');
    file.write(str(priceGoblinMail) + '\n');
    file.write(str(priceHugeBone) + '\n');
    file.write(str(priceDragonHide) + '\n');
    file.write(str(priceRunicTablet) + '\n');
    file.write(str(pricePotion) + '\n');
    file.write(str(priceIngot) + '\n');
    file.write(str(priceFood) + '\n');
    file.write(str(priceRawFood) + '\n');
    file.write(str(priceBait) + '\n');
    file.write(str(priceSeed) + '\n');
    file.write(str(priceFur) + '\n');
    file.write(str(priceOre) + '\n');
    file.write(str(priceBow) + '\n');
    file.write(str(priceLog) + '\n');
    file.write(str(priceGemstone) + '\n');
    file.write(str(priceMagicOrb) + '\n');
    file.write(str(Woodcuttinglvl) + '\n');
    file.write(str(Woodcuttingxpgain) + '\n');
    file.write(str(Woodcuttingcurxp) + '\n');
    file.write(str(Woodcuttingxpleft) + '\n');
    file.write(str(Cooklvl) + '\n');
    file.write(str(Cookxpremain) + '\n');
    file.write(str(Cookxpgain) + '\n');
    file.write(str(Cookcurxp) + '\n');
    file.write(str(Cookxpleft) + '\n');
    file.write(str(Fishinglvl) + '\n');
    file.write(str(Fishingxpremain) + '\n');
    file.write(str(Fishingxpgain) + '\n');
    file.write(str(Fishingcurxp) + '\n');
    file.write(str(Fishingxpleft) + '\n');
    file.write(str(Mininglvl) + '\n');
    file.write(str(Miningxpremain) + '\n');
    file.write(str(Miningxpgain) + '\n');
    file.write(str(Miningcurxp) + '\n');
    file.write(str(Miningxpleft) + '\n');
    file.write(str(Smithinglvl) + '\n');
    file.write(str(Smithingxpremain) + '\n');
    file.write(str(Smithingxpgain) + '\n');
    file.write(str(Smithingcurxp) + '\n');
    file.write(str(Smithingxpleft) + '\n');
    file.write(str(Thievinglvl) + '\n');
    file.write(str(Thievingxpremain) + '\n');
    file.write(str(Thievingxpgain) + '\n');
    file.write(str(Thievingcurxp) + '\n');
    file.write(str(Thievingxpleft) + '\n');
    file.write(str(ttllvl) + '\n');
    file.close();
    MENU();
#Login System
def login():
    global username
    global password
    global bankAccount1Gold;
    global bankAccount1Message;
    global bankAccount2Gold;
    global bankAccount2Message;
    global bankAccount3Gold;
    global bankAccount3Message;
    global bankAccount4Gold;
    global bankAccount4Message;
    global bankAccount5Gold;
    global bankAccount5Message;
    global cost;
    global cost1;
    global gcho;
    global dmgnpc;
    global ls1;
    global killcount;
    global ls2;
    global la1;
    global la2;
    global HP;
    global maxHP;
    global armtype;
    global swordtype;
    global skind;
    global buyword1;
    global buyword2;
    global currentLevel;
    global aan;
    global bankchoice;
    global bankgold;
    global swordchoice;
    global swordchoice2;
    global swordchoice3;
    global swordexist;
    global sprice;
    global armchoice;
    global armchoice;
    global aprice;
    global playerxp;
    global xpuntil;
    global origxp;
    global money;
    global key;
    global damage;
    global dr;
    global goblinMail;
    global hugeBone;
    global dragonHide;
    global runicTablet;
    global food;
    global rawFood;
    global bait;
    global ea;
    global potion;
    global ingot;
    global seed;
    global bow;
    global fur;
    global gemstone;
    global log;
    global ore;
    global magicOrb;
    global clothArmor;
    global chainArmor;
    global ironArmor;
    global steelArmor;
    global crystalArmor;
    global sacredArmor;
    global infernalArmor;
    global arm8;
    global arm9;
    global arm10;
    global arm11;
    global arm12;
    global ma1;
    global ma2;
    global ma3;
    global ma4;
    global ma5;
    global ma6;
    global ma7;
    global ma8;
    global ma9;
    global ma10;
    global ms1;
    global ms2;
    global ms3;
    global ms4;
    global ms5;
    global ms6;
    global ms7;
    global ms8;
    global ms9;
    global ms10;
    global woodenSword;
    global stoneSword;
    global ironSword;
    global steelSword;
    global crystalSword;
    global sacredBlade;
    global infernalRapier;
    global omegaMaul;
    global mythicalGodsword;
    global sword10;
    global sword11;
    global sword12;
    global priceGoblinMail;
    global priceHugeBone;
    global priceDragonHide;
    global priceRunicTablet;
    global pricePotion;
    global priceFood;
    global priceIngot;
    global priceSeed;
    global priceRawFood;
    global priceBait;
    global priceFur;
    global priceOre;
    global priceLog;
    global priceGemstone;
    global priceBow;
    global priceMagicOrb;
    global Woodcuttinglvl;
    global Woodcuttingxpremain;
    global Woodcuttingxpgain;
    global Woodcuttingcurxp;
    global Woodcuttingxpleft;
    global Cooklvl;
    global Cookxpremain;
    global Cookxpgain;
    global Cookcurxp;
    global Cookxpleft;
    global Fishinglvl;
    global Fishingxpremain;
    global Fishingxpgain;
    global Fishingcurxp;
    global Fishingxpleft;
    global Mininglvl;
    global Miningxpremain;
    global Miningxpgain;
    global Miningcurxp;
    global Miningxpleft;
    global Smithinglvl;
    global Smithingxpremain;
    global Smithingxpgain;
    global Smithingcurxp;
    global Smithingxpleft;
    global Thievinglvl;
    global Thievingxpremain;
    global Thievingxpgain;
    global Thievingcurxp;
    global Thievingxpleft;
    global ttllvl;
    os.system('cls')
    username = input('Enter username: ');
    #try:
    file = open(username + '.rrcs','r');
    #Username/Password
    username = str(file.readline());
    password = str(file.readline());
    #Bank Accounts/Money
    bankAccount1Gold = str(file.readline());
    bankAccount1Message = str(file.readline());
    bankAccount2Gold = str(file.readline());
    bankAccount2Message = str(file.readline());
    bankAccount3Gold = str(file.readline());
    bankAccount3Message = str(file.readline());
    bankAccount4Gold = str(file.readline());
    bankAccount4Message = str(file.readline());
    bankAccount5Gold = str(file.readline());
    bankAccount5Message = str(file.readline());
    cost1 = str(file.readline());
    cost = str(file.readline());
    gcho = str(file.readline());
    dmgnpc = str(file.readline());
    ls1 = str(file.readline());
    ls2 = str(file.readline());
    la1 = str(file.readline());
    la2 = str(file.readline());
    armtype = str(file.readline());
    HP = str(file.readline());
    maxHP = str(file.readline());
    swordtype = str(file.readline());
    skind = str(file.readline());
    currentLevel = str(file.readline());
    origxp = str(file.readline());
    playerxp = str(file.readline());
    xpuntil = str(file.readline());
    swordchoice = str(file.readline());
    swordchoice2 = str(file.readline());
    swordchoice3 = str(file.readline());
    swordexist = str(file.readline());
    sprice = str(file.readline());
    armchoice = str(file.readline());
    armchoice2 = str(file.readline());
    aprice = str(file.readline());
    money = str(file.readline());
    key = str(file.readline());
    damage = str(file.readline());
    killcount = str(file.readline());
    dr = str(file.readline());
    goblinMail = str(file.readline());
    hugeBone = str(file.readline());
    dragonHide = str(file.readline());
    runicTablet = str(file.readline());
    food = str(file.readline());
    rawFood = str(file.readline());
    potion = str(file.readline());
    bait = str(file.readline());
    seed = str(file.readline());
    fur = str(file.readline());
    gemstone = str(file.readline());
    ingot = str(file.readline());
    log = str(file.readline());
    bow = str(file.readline());
    ore = str(file.readline());
    aan = str(file.readline());
    bankchoice = str(file.readline());
    magicOrb = str(file.readline());
    clothArmor = str(file.readline());
    chainArmor = str(file.readline());
    ironArmor = str(file.readline());
    steelArmor = str(file.readline());
    crystalArmor = str(file.readline());
    sacredArmor = str(file.readline());
    infernalArmor = str(file.readline());
    arm8 = str(file.readline());
    arm9 = str(file.readline());
    arm10 = str(file.readline());
    arm11 = str(file.readline());
    arm12 = str(file.readline());
    ma1 = str(file.readline());
    ma2 = str(file.readline());
    ma3 = str(file.readline());
    ma4 = str(file.readline());
    ma5 = str(file.readline());
    ma6 = str(file.readline());
    ma7 = str(file.readline());
    ma8 = str(file.readline());
    ma9 = str(file.readline());
    ma10 = str(file.readline());
    ms1 = str(file.readline());
    ms2 = str(file.readline());
    ms3 = str(file.readline());
    ms4 = str(file.readline());
    ms5 = str(file.readline());
    ms6 = str(file.readline());
    ms7 = str(file.readline());
    ms8 = str(file.readline());
    ms9 = str(file.readline());
    ms10 = str(file.readline());
    woodenSword = str(file.readline());
    stoneSword = str(file.readline());
    ironSword = str(file.readline());
    steelSword = str(file.readline());
    crystalSword = str(file.readline());
    sacredBlade = str(file.readline());
    infernalRapier = str(file.readline());
    omegaMaul = str(file.readline());
    mythicalGodsword = str(file.readline());
    sword10 = str(file.readline());
    sword11 = str(file.readline());
    sword12 = str(file.readline());
    priceGoblinMail = str(file.readline());
    priceHugeBone = str(file.readline());
    priceDragonHide = str(file.readline());
    priceRunicTablet = str(file.readline());
    pricePotion = str(file.readline());
    priceIngot = str(file.readline());
    priceFood = str(file.readline());
    priceRawFood = str(file.readline());
    priceBait = str(file.readline());
    priceSeed = str(file.readline());
    priceFur = str(file.readline());
    priceOre = str(file.readline());
    priceBow = str(file.readline());
    priceLog = str(file.readline());
    priceGemstone = str(file.readline());
    priceMagicOrb = str(file.readline());
    Woodcuttinglvl = str(file.readline());
    Woodcuttingxpgain = str(file.readline());
    Woodcuttingcurxp = str(file.readline());
    Woodcuttingxpleft = str(file.readline());
    Cooklvl = str(file.readline());
    Cookxpremain = str(file.readline());
    Cookxpgain = str(file.readline());
    Cookcurxp = str(file.readline());
    Cookxpleft = str(file.readline());
    Fishinglvl = str(file.readline());
    Fishingxpremain = str(file.readline());
    Fishingxpgain = str(file.readline());
    Fishingcurxp = str(file.readline());
    Fishingxpleft = str(file.readline());
    Mininglvl = str(file.readline());
    Miningxpremain = str(file.readline());
    Miningxpgain = str(file.readline());
    Miningcurxp = str(file.readline());
    Miningxpleft = str(file.readline());
    Smithinglvl = str(file.readline());
    Smithingxpremain = str(file.readline());
    Smithingxpgain = str(file.readline());
    Smithingcurxp = str(file.readline());
    Smithingxpleft = str(file.readline());
    Thievinglvl = str(file.readline());
    Thievingxpremain = str(file.readline());
    Thievingxpgain = str(file.readline());
    Thievingcurxp = str(file.readline());
    Thievingxpleft = str(file.readline());
    ttllvl = str(file.readline());

   

    file.close;
    print(password)
    pass1 = str(input('Enter your password: '));
    if pass1 != str(password):
        print('Incorrect Password.');
        time.sleep(1);
        entergame();
    MENU()
    #except FileNotFoundError:
        #print('User does not exist');
        #time.sleep(1);
        #entergame();

entergame();
