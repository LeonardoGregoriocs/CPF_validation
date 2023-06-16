from app.service.analyze_data_service import AnalyzeDataService

def test_validator_cpf_when_cpf_is_valid():
    analyze_data = AnalyzeDataService()

    cpf = '12365487982'
    result = analyze_data.validator_cpf(cpf)

    assert result is True
