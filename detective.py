import pandas as pd
import time

print("[+] در حال بارگذاری ماژول‌های امنیتی...")
time.sleep(1)

# تعریف آدرس‌های واقعی هک رونین (آفلاین و بدون نیاز به شبکه)
LAZARUS_WALLET = "0x098B716B8Aaf21512996dC57EB0615e2383E2f96"
TORNADO_CASH_MIXER = "0x47ac56a6123b262e12d997d6a1170b6890f5a7a1"

# شبیه‌سازی دیتابیس تراکنش‌های واقعی گروه لازاروس بعد از هک
blockchain_data = {
    'Transaction_ID': ['0xaa12...', '0xbb34...', '0xcc56...', '0xdd78...'],
    'From_Address': [LAZARUS_WALLET, LAZARUS_WALLET, LAZARUS_WALLET, "0x1111..."],
    'To_Address': [TORNADO_CASH_MIXER, TORNADO_CASH_MIXER, "0x9999...", TORNADO_CASH_MIXER],
    'Amount_ETH': [5000, 3500, 120, 450],
    'Status': ['Flagged', 'Flagged', 'Normal', 'Normal']
}

df = pd.DataFrame(blockchain_data)

print("[+] دیتابیس آفلاین بلاک‌چین با موفقیت بارگذاری شد.")
print(f"[!] هدف تحت نظر: ولت گروه لازاروس ({LAZARUS_WALLET})")
print("-" * 60)
time.sleep(1)

# الگوریتم کارآگاهی پایتون برای فیلتر کردن تراکنش‌های مشکوک هکر
def track_hacker_funds(wallet_address, database):
    print("[*] در حال اجرای الگوریتم ردیابی دارایی‌های سرقت شده...")
    time.sleep(1.5)
    hacker_txs = database[database['From_Address'] == wallet_address]
    laundering_txs = hacker_txs[hacker_txs['To_Address'] == TORNADO_CASH_MIXER]
    return laundering_txs

# اجرای الگوریتم و چاپ خروجی
suspicious_activities = track_hacker_funds(LAZARUS_WALLET, df)

print("\n🚨🚨🚨 [هشدار امنیتی: تراکنش‌های مشکوک یافت شد!] 🚨🚨🚨")
print(suspicious_activities[['Transaction_ID', 'To_Address', 'Amount_ETH']])

total_laundered = suspicious_activities['Amount_ETH'].sum()
print(f"\n[📊] آمار کارآگاهی: هکر مجموعاً {total_laundered} اتریوم را به ماشین پول‌شویی فرستاده است.")




import pandas as pd
import time

print("[+] در حال بارگذاری سیستم کارآگاهی Shadow Economy...")
time.sleep(1)

# ۱. بیس دیتای آفلاین هک رونین
LAZARUS_WALLET = "0x098B716B8Aaf21512996dC57EB0615e2383E2f96"
TORNADO_CASH_MIXER = "0x47ac56a6123b262e12d997d6a1170b6890f5a7a1"

blockchain_data = {
    'Transaction_ID': ['0xaa12...', '0xbb34...', '0xcc56...', '0xdd78...'],
    'From_Address': [LAZARUS_WALLET, LAZARUS_WALLET, LAZARUS_WALLET, "0x1111..."],
    'To_Address': [TORNADO_CASH_MIXER, TORNADO_CASH_MIXER, "0x9999...", TORNADO_CASH_MIXER],
    'Amount_ETH': [5000, 3500, 120, 450],
    'Status': ['Flagged', 'Flagged', 'Normal', 'Normal']
}
df = pd.DataFrame(blockchain_data)

# ۲. فیلترینگ تراکنش‌ها توسط پایتون
hacker_txs = df[df['From_Address'] == LAZARUS_WALLET]
laundering_txs = hacker_txs[hacker_txs['To_Address'] == TORNADO_CASH_MIXER]
total_laundered = laundering_txs['Amount_ETH'].sum()

print("[+] فیلترینگ دیتای بلاک‌چین به پایان رسید.")
print("[*] در حال فعال‌سازی AI Agent برای کالبدشکافی داستانی پرونده...")
print("-" * 60)
time.sleep(2)

# ۳. کلاس ایجنت هوش مصنوعی (AI Cyber Investigative Agent)
class AICyberAgent:
    def __init__(self, wallet, target, amount, tx_count):
        self.wallet = wallet
        self.target = target
        self.amount = amount
        self.tx_count = tx_count

    def generate_investigative_report(self):
        # پرامپت مژندسی‌شده برای تولید گزارش افشاگرانه
        report = f"""
======================================================================
🕵️‍♂️ SHADOW ECONOMY - AI INVESTIGATIVE AGENT REPORT 🕵️‍♂️
======================================================================
[THE LAZARUS GROUP: INSIDE THE INTEL]

The blockchain never forgets, and today, our AI agent has successfully 
cracked open the digital footsteps of the world's most elusive cyber 
syndicate: The Lazarus Group.

Here is the behind-the-scenes reality of the $620M Ronin Heist:

1. THE TARGET RETREAT:
   Our system caught the hacker's primary wallet ({self.wallet}) 
   initiating {self.tx_count} massive outbound movements. They weren't just 
   moving funds; they were running away from international cyber-police.

2. THE LAUNDERING MACHINE:
   The funds didn't go to an exchange. The AI flagged a total of 
   [{self.amount} ETH] flowing directly into the darkness of Tornado Cash 
   ({self.target}). This is where clean crypto goes to die and anonymous 
   cash is born.

3. THE JOURNALIST VERDICT:
   What we are witnessing is not a simple hack; it is state-sponsored 
   financial warfare. By routing exactly {self.amount} ETH through mixers, 
   Lazarus attempted to erase their shadows. But our Python algorithm 
   just proved that code can always catch the thief.

STATUS: CASE ANALYSIS COMPLETE // REPORT GENERATED SUCCESSFULLY.
======================================================================
"""
        return report

# ۴. فراخوانی ایجنت و چاپ گزارش در ترمینال
agent = AICyberAgent(
    wallet=LAZARUS_WALLET, 
    target=TORNADO_CASH_MIXER, 
    amount=total_laundered, 
    tx_count=len(laundering_txs)
)

report_output = agent.generate_investigative_report()

# شبیه‌سازی افکت تایپ شدن گزارش توسط هوش مصنوعی برای جذابیت بصری
for line in report_output.split('\n'):
    print(line)
    time.sleep(0.15) # یک تاخیر کوچک برای حس زنده بودن هوش مصنوعی