from requests import get
from xml.etree import ElementTree as ET
import unicodedata

from domain.entities.LocaleForecast import LocaleForecast

from domain.repositories.forecast import ForecastRepository

from app.exceptions.locale_not_found import LocaleNotFound

FORECAST_DATA_URL = 'http://servicos.cptec.inpe.br/XML'
LOCALE_DATA_URL = 'https://viacep.com.br/ws'

class APIForecastRepository(ForecastRepository):
    def get_forecast(self, locale_cep: str) -> dict:
        response = get(f'{LOCALE_DATA_URL}/{locale_cep}/json/')

        if response.status_code != 200:
            raise LocaleNotFound(locale_cep)
        
        info = response.json()
        
        if info.get('erro') == True:
            raise LocaleNotFound(locale_cep)

        locale_data = {
            'neighborhood': info.get('bairro'),
            'cep': info.get('cep'),
            'complement': info.get('complemento'),
            'ddd_code': info.get('ddd'),
            'gia_code': info.get('gia'),
            'ibge_code': info.get('ibge'),
            'name': info.get('localidade'),
            'address': info.get('logradouro'),
            'siafi_code': info.get('siafi'),
            'uf': info.get('uf')
        }

        locale_name = unicodedata.normalize('NFKD', locale_data.get('name')).encode('ASCII', 'ignore').decode('ASCII')

        locale_info_response = get(f'{FORECAST_DATA_URL}/listaCidades', params={
            'city': locale_name
        })

        locale_root_element = ET.ElementTree(ET.fromstring(locale_info_response.text)).getroot()
        locale_id = locale_root_element[0][2].text

        forecast_response = get(f'{FORECAST_DATA_URL}/cidade/{locale_id}/previsao.xml')
        forecast_root_element = ET.ElementTree(ET.fromstring(forecast_response.text)).getroot()

        four_day_forecast = [{
            'date': str(x.find('dia').text),
            'weather': str(x.find('tempo').text),
            'max': str(x.find('maxima').text),
            'min': str(x.find('minima').text),
            'iuv': str(x.find('iuv').text)} for x in forecast_root_element.findall('previsao')] 

        forecast_data = {
            'name': str(forecast_root_element.find('nome').text),
            'uf': str(forecast_root_element.find('uf').text),
            'updated_at': str(forecast_root_element.find('atualizacao').text),
            'forecasts': four_day_forecast
        }

        return LocaleForecast(locale_data, forecast_data)
        