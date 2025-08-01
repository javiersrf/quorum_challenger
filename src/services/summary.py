import csv


def generate_legislators_summary(
    legislators: dict[str, list], vote_results: dict[str, list], output: str = "./"
):
    data = {}
    for idx, legislator in enumerate(legislators["id"]):
        data[legislator] = {
            "legislator_id": legislator,
            "legislator_name": legislators["name"][idx],
            "sponsored_bills": 0,
            "opposed_bills": 0,
        }
    for idx, _ in enumerate(vote_results["vote_id"]):
        legislator_id = vote_results["legislator_id"][idx]
        vote_type = vote_results["vote_type"][idx]
        if legislator_id not in data:
            continue
        if vote_type == "1":
            data[legislator_id]["sponsored_bills"] += 1
        elif vote_type == "2":
            data[legislator_id]["opposed_bills"] += 1
    final_path = output + "legislators-support-oppose-count.csv"
    with open(
        final_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as csvfile:
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
    return final_path


def generate_bill_summary(
    bills: dict[str, list],
    votes: dict[str, list],
    vote_results: dict[str, list],
    output: str = "./",
):
    data = {}
    votes_bill_map = {}
    for idx, vote in enumerate(votes["id"]):
        votes_bill_map[vote] = votes["bill_id"][idx]
    for idx, bill in enumerate(bills["id"]):
        data[bill] = {
            "bills_id": bill,
            "bills_title": bills["title"][idx],
            "primary_sponsor": bills["sponsor_id"][idx],
            "sponsored_bills": 0,
            "opposed_bills": 0,
        }
    for idx, vote_result in enumerate(vote_results["vote_id"]):
        bill_id = votes_bill_map[vote_result]
        vote_type = vote_results["vote_type"][idx]
        if vote_type == "1":
            data[bill_id]["sponsored_bills"] += 1
        elif vote_type == "2":
            data[bill_id]["opposed_bills"] += 1
    final_path = output + "bills-support-oppose-count.csv"
    with open(final_path, "w", newline="", encoding="utf-8") as csvfile:
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
    return final_path
