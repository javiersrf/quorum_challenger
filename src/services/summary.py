import click
import csv


def generate_legislators_summary(
    legislators: dict[str, list], vote_results: dict[str, list]
):
    data = {}
    for idx, legislator in enumerate(legislators["id"]):
        data[legislator] = {
            "legislator_id": legislator,
            "legislator_name": legislators["name"][idx],
            "sponsored_bills": 0,
            "opposed_bills": 0,
        }
    for vote_result in vote_results["vote_id"]:
        legislator_id = vote_result["legislator_id"]
        vote_type = vote_result["vote_type"]
        if vote_type == 1:
            data[legislator_id]["sponsored_bills"] += 1
        elif vote_type == 2:
            data[legislator_id]["opposed_bills"] += 1
    with open("legislators_summary.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "legislator_id",
            "legislator_name",
            "sponsored_bills",
            "opposed_bills",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data.values():
            writer.writerow(row)
    return list(data.values())


def generate_bill_summary(
    bills: dict[str, list], votes: dict[str, list], vote_results: dict[str, list]
):
    data = {}
    votes_bill_map = {vote["id"]: vote["bill_id"] for vote in votes["id"]}
    for idx, bill in enumerate(bills["id"]):
        data[bill] = {
            "bills_id": bill,
            "bills_title": bills["title"][idx],
            "primary_sponsor": bills["sponsor_id"][idx],
            "sponsored_bills": 0,
            "opposed_bills": 0,
        }
    for vote_result in vote_results["vote_id"]:
        bill_id = votes_bill_map[vote_result["vote_id"]]
        vote_type = vote_result["vote_type"]
        if vote_type == 1:
            data[bill_id]["sponsored_bills"] += 1
        elif vote_type == 2:
            data[bill_id]["opposed_bills"] += 1

    with open("bills_summary.csv", "w", newline="") as csvfile:
        fieldnames = [
            "bills_id",
            "bills_title",
            "primary_sponsor",
            "sponsored_bills",
            "opposed_bills",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data.values():
            writer.writerow(row)
    return list(data.values())
