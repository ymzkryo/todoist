class Certification:
    def load_json(self):
        """
        load json file to API_TOKEN
        
        Returns
        -------
        json_data['api_token'] : string
            json file api_token
        """
        import json
        f = open('./todoist/config.json', 'r')
        json_data = json.load(f)
        f.close()
        return json_data['api_token']
