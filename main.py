import sys
from pathlib import Path

# Add the les_portageurs_web_scrapping project to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "les_portageurs_web_scrapping" / "src"))
# Add the pricedropcheck project to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "pricedropcheck" / "src"))

from apscheduler.schedulers.blocking import BlockingScheduler

import price_drop_checker
import portageurs

run_price_dropcheck = price_drop_checker.price_drop_checker
scrape_lesportageurs = portageurs.scrape_lesportageurs

scheduler = BlockingScheduler()

# PriceDropCheck : toutes les 8 heures
run_price_dropcheck()
scheduler.add_job(
    run_price_dropcheck,
    "interval",
    hours=4,
    max_instances=1
)

# Les Portageurs : toutes les 45 minutes
scrape_lesportageurs()
scheduler.add_job(
    scrape_lesportageurs,
    "interval",
    minutes=60*2,
    max_instances=1
)

scheduler.start()