from services.reporting_service import ReportingService


def test_common_report(capsys, show_common_report_mocker):
    reporting_service_obj, text_for_print = show_common_report_mocker
    reporting_service_obj.show_common_report()
    out_flow = capsys.readouterr().out.rstrip()
    assert out_flow == text_for_print


def test_show_bill(capsys):
    text_for_print = "bill here"
    ReportingService.show_bill(text_for_print)
    out_flow = capsys.readouterr().out.rstrip()
    assert out_flow == text_for_print