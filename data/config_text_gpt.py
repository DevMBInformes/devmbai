from .obj_table import obj_table
from urllib.parse import urlparse

class config_text_gpt(obj_table):

    def values_default(self)->None:
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
        self.id = 'ip'
        self.url = 't'
        self.model = 't'
        self.n = 'i'
        self.max_tokens = 'i'
        self.stream = 'i' #TvF
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

    def set_id(self, _id)->None:
        self.id = _id
        return None

    def set_url(self, _url)->bool:
        ''' We check if it is a correctly composed url, 
        otherwise it returns false. This does not imply 
        that the address being accessed is correct, 
        simply that it is well composed.
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

    def set_model(self, _model)->None:
        '''
        later we will have to check if the model exists.
        '''
        self.model = _model 
        return None

    def set_n(self, _n)->None:
        self.n = _n
        return None

    def set_max_tokens(self, n_tokens)->None:
        pass

    def set_top_p(self, _top_p)->None:
        pass

        
