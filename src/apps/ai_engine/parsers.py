class ResponseParser:

    @staticmethod
    def parse_improved_content(response: str) -> dict:
        try:
            lines = response.strip().split('\n')
            title, body = '', []
            in_body = False
            for line in lines:
                if line.startswith('TITLE:'):
                    title = line.replace('TITLE:', '').strip()
                elif line.startswith('BODY:'):
                    in_body = True
                    body.append(line.replace('BODY:', '').strip())
                elif in_body:
                    body.append(line)
            return {'title': title, 'body': '\n'.join(body).strip()}
        except Exception:
            return {'title': '', 'body': response}

    @staticmethod
    def parse_summary(response: str) -> str:
        return response.strip()

    @staticmethod
    def parse_status_suggest(response: str) -> dict:
        try:
            parts = response.strip().split(' ', 1)
            ready = parts[0].upper() == 'YES'
            reason = parts[1] if len(parts) > 1 else ''
            return {'ready': ready, 'reason': reason}
        except Exception:
            return {'ready': False, 'reason': response}
    
    @staticmethod
    def parse_caption(response: str) -> str:
        return response.strip()
    
    @staticmethod
    def parse_adapted_content(response: str) -> str:
        return response.strip()
    
    @staticmethod
    def parse_hashtags(response: str) -> dict:
        try:
            lines = response.strip().split('\n')
            hashtags, seo_tags = '', ''
            for line in lines:
                if line.startswith('HASHTAGS:'):
                    hashtags = line.replace('HASHTAGS:', '').strip()
                elif line.startswith('SEO_TAGS:'):
                    seo_tags = line.replace('SEO_TAGS:', '').strip()
            return {'hashtags': hashtags, 'seo_tags': seo_tags}
        except Exception:
            return {'hashtags': '', 'seo_tags': response}