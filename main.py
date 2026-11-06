import sys
from pathlib import Path

# Add the les_portageurs_web_scrapping project to the path
sys.path.insert(0, str(Path(__file__).parent.parent / "les_portageurs_web_scrapping"))

from apscheduler.schedulers.blocking import BlockingScheduler

# from src.main import main as run_price_dropcheck
from src.portageurs import scrape_lesportageurs

scheduler = BlockingScheduler()

# PriceDropCheck : toutes les 8 heures
# scheduler.add_job(
#     run_price_dropcheck,
#     "interval",
#     hours=8,
#     max_instances=1
# )

# Les Portageurs : toutes les 45 minutes
scrape_lesportageurs()
scheduler.add_job(
    scrape_lesportageurs,
    "interval",
    minutes=45,
    max_instances=1
)

scheduler.start()