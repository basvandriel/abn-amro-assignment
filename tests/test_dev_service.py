from abn_assignment.domain.developer.service import Service


def test_save_from_so():
    service = Service()
    service.save_from_stackoverflow()
