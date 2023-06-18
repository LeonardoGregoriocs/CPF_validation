from app.service.analyze_data_service import AnalyzeDataService

def test_validator_cpf_when_cpf_is_valid():
    analyze_data = AnalyzeDataService()

    cpf = '12365487982'
    result = analyze_data.clean_and_validator_cpf(cpf)

    assert result == cpf

def test_validator_cpf_when_cpf_is_not_valid():
    analyze_data = AnalyzeDataService()

    cpf = '123654879'
    result = analyze_data.clean_and_validator_cpf(cpf)

    assert result is False

def test_validator_cnpj_when_cnpj_is_valid():
    analyze_data = AnalyzeDataService()

    cnpj = '21340472000163'
    result = analyze_data.clean_and_validator_cnpj(cnpj)

    assert result == cnpj

def test_validator_cnpj_when_cnpj_is_not_valid():
    analyze_data = AnalyzeDataService()

    cnpj = '21340472000163'
    result = analyze_data.clean_and_validator_cnpj(cnpj)

    assert result is False
