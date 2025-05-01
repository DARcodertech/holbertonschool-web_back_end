#!/usr/bin/env python3
"""
return a list
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a list"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """class a server"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init a dataset"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """return a dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8-sig") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a dataset"""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': (
                        page + 1 if (page * page_size) < total_items else None
                        ),
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
