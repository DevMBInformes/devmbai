from .obj_table import obj_table
from .obj_sqlite import obj_sqlite
from urllib.parse import urlparse

class config_text_gpt(obj_table):

    def values_default(self)->None:
        self.name = 'configDefault3'
        self.url = "https://api.openai.com/v1/completions"
        self.temperature = 0.3
        self.model = "text-davinci-002"
        self.n = 1
        self.max_tokens = 600
        self.top_p = 1.0
        self.stream = 0
        self.logprobs = 0
        self.stop = ""
        self.suffix = ""
        self.echo = 0
        self.presence_penalty = 0
        self.frequency_penalty = 0
        self.best_of = 1
        self.logit_bias = ""
        self.user = ""
        return None

    def values_table(self)->None:
        self.id = 'ip' # ok
        self.name = 'tu' #ok
        self.url = 't' #ok
        self.model = 't' #ok
        self.n = 'i' #ok
        self.max_tokens = 'i' #ok
        self.stream = 'i' #TvF #ok
        self.logprobs = 'i'
        self.stop = 't'
        self.suffix = 't'
        self.echo = 'i' #TvF
        self.logit_bias = 't'
        self.user = 't'
        self.temperature = 'r'
        self.top_p = 'r'
        self.presence_penalty = 'r'
        self.frequency_penalty = 'r'
        self.best_of = 'r'
        return None


    #block of properties

    def set_id(self, _id:int)->None:
        '''set_id: set a id.

        :param _id: int - whole number that reference a id object's
        
        :return None - Is method.
        '''
        self.id = _id
        return None

    def set_name(self, _name:str)->None:
        '''set_name: set configuration name
        this values is unique

        :param _name: str - configuration name

        :return: None - is a method
        '''


    def set_url(self, _url)->bool:
        '''set_url: We check if it is a correctly composed url, 
        otherwise it returns false.
        
        :param _url: str - string with url the openai

        :return: bool - Return True if the url is correct your form
        '''
        try:
            result = urlparse(_url)
            if all([result.scheme, result.netloc]):
                self.url = _url
                return True
            else:
                return False
        except ValueError:
            return False

    def set_model(self, _model:str)->None:
        '''set_model: later we will have to check if the model exists.

        :param _model:str - name of model.

        :return: None - Is method.
        '''
        self.model = _model 
        return None

    def set_n(self, _n:int)->None:
        '''set_n: Set n, n is the number response.
        
        :param _n: int - number of response.

        :return: None - Is method.
        '''
        self.n = _n
        return None

    def set_max_tokens(self, n_tokens:int)->bool:
        '''set_max_tokens: maximum number of tokens 
        that we want to receive in the response.

        :param n_tokens: int - value between 1 and 4096
        
        :return: bool - if the value is > 1 and < a 4096
        '''
        if n_tokens > 1 and n_tokens < 0:
            self.max_tokens = n_tokens
            return True
        return False

    def set_top_p(self, _top_p:float)->bool:
        '''set_top_p: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

        :param _top_p: float - float number between 0 and 1 

        :return: None - is method

        '''
        if _top_p > 0 and _top_p < 1:
            self.top_p = _top_p
            return True
        return False

    def set_stream(self, _stream:int)->None:
        '''set_stream: if the response is received 
        as it is generated, or False if it is expected to finish

        :param _stream: int - convert to zero or one any value.

        :return: None - is method
        '''
        self.stream = int(bool(_stream))
        return None

    def set_logit_bias(self, _logit_bias:str)->None:
        '''set_logit_bias

        :param: -

        :return: -
        '''
        return None

    def set_logprobs(self, _logprobs:int)->None:
        '''set_logprobs: Include the log probabilities on
        the logprobas most likely token. i.e, if logprobs
        is 5, the API will return a list of the 5 most likely.

        :param _logprobs: -

        :return: None - is a method
        '''
        
        return None

    def set_echo(self, _echo)->None:
        '''set_echo

        :param: -

        :return: -
        '''
        return None


    def set_stop(self, str_stop:str)->None:
        '''set_stop: set string of 4 values.

        :param str_stop: str - string of 4 values
        indicating to end the response

        :return: None - is method
        '''
        self.value = set_stop[:4]
        return None


    def _convert_to_bool(self, value:int)->bool:
        '''_convert_to_bool: convert any int in True or False

        :param: int - any value int

        :return: bool - modified value
        '''
        return bool(value)


    def record_default_values(self) -> bool:
        values_default = self.prepare_values_default()
        obj_sql = obj_sqlite(self._data_base)
        count = obj_sql.selectOne(self.get_name(), f'name="{values_default["name"]}"',with_names=False)
        if len(count)==0:
            obj_sql.insert(self.get_name(),values_default)
            return True
        else:
            return False
