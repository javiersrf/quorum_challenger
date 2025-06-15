import pytest
import os
from src.services import summary
import click
from unittest import mock
from unittest.mock import patch, mock_open


def test_generate_legislators_summary():
    input_legislators: dict[str, list] = {
        "id": [904789, 412649, 400380],
        "name": [
            "Rep. Don Bacon (R-NE-2)",
            "Rep. Jeff Van Drew (R-NJ-2)",
            "Rep. Ilhan Omar (D-MN-5)",
        ],
    }
    input_vote_results: dict[str, list] = {
        "id": [
            92516784,
            92516770,
            92516768,
            92516753,
            92516734,
            92516711,
            92516702,
            92516703,
        ],
        "legislator_id": [400440, 17941, 904789, 400380, 412649, 400380, 15367, 400380],
        "vote_id": [
            3321166,
            3321166,
            3321166,
            3321166,
            3321166,
            3321166,
            3321166,
            3321167,
        ],
        "vote_type": [2, 2, 2, 2, 1, 1, 2, 2],
    }

    expected_output = [
        {
            "legislator_id": 904789,
            "legislator_name": "Rep. Don Bacon (R-NE-2)",
            "sponsored_bills": 0,
            "opposed_bills": 1,
        },
        {
            "legislator_id": 412649,
            "legislator_name": "Rep. Jeff Van Drew (R-NJ-2)",
            "sponsored_bills": 1,
            "opposed_bills": 0,
        },
        {
            "legislator_id": 400380,
            "legislator_name": "Rep. Ilhan Omar (D-MN-5)",
            "sponsored_bills": 1,
            "opposed_bills": 2,
        },
    ]

    with (
        patch("src.services.summary.open", create=True),
    ):
        result = summary.generate_legislators_summary(
            legislators=input_legislators, vote_results=input_vote_results
        )
        assert result == expected_output


def test_generate_bills_summary():
    input_bills: dict[str, list] = {
        "id": [
            2952375,
            2900994,
        ],
        "title": [
            "H.R. 5376: Build Back Better Act",
            "H.R. 3684: Infrastructure Investment and Jobs Act",
        ],
        "sponsor_id": [412211, 400100],
    }
    input_votes: dict[str, list] = {
        "id": [
            3314452,
            3321166,
        ],
        "bill_id": [
            2900994,
            2952375,
        ],
    }
    input_vote_results: dict[str, list] = {
        "id": [
            92516784,
            92516770,
            92516768,
            92516753,
            92516734,
            92516711,
            92516702,
            92516703,
        ],
        "legislator_id": [400440, 17941, 904789, 400380, 412649, 400380, 15367, 400380],
        "vote_id": [
            3321166,
            3321166,
            3321166,
            3321166,
            3314452,
            3321166,
            3321166,
            3314452,
        ],
        "vote_type": [2, 2, 2, 2, 1, 1, 2, 2],
    }

    expected_output = [
        {
            "bills_id": 2952375,
            "bills_title": "H.R. 5376: Build Back Better Act",
            "primary_sponsor": 412211,
            "sponsored_bills": 1,
            "opposed_bills": 5,
        },
        {
            "bills_id": 2900994,
            "bills_title": "H.R. 3684: Infrastructure Investment and Jobs Act",
            "primary_sponsor": 400100,
            "sponsored_bills": 1,
            "opposed_bills": 1,
        },
    ]

    with (
        patch("src.services.summary.open", create=True),
    ):
        result = summary.generate_bill_summary(
            bills=input_bills, vote_results=input_vote_results, votes=input_votes
        )
        assert result == expected_output
