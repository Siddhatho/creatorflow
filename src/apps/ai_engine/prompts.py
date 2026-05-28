class PromptManager:

    @staticmethod
    def content_improve(title: str, body: str) -> str:
        return f"""
You are a content strategist. Improve the following content.
Keep the same intent but make it more engaging and professional.

Title: {title}
Body: {body}

Return improved title and body only. Format:
TITLE: <improved title>
BODY: <improved body>
"""

    @staticmethod
    def content_summarize(body: str) -> str:
        return f"""
Summarize the following content in 2-3 sentences.

Content: {body}

Return only the summary.
"""

    @staticmethod
    def status_suggest(title: str, body: str) -> str:
        return f"""
You are a content reviewer. Based on this content, is it ready for publishing?
Reply with one word: YES or NO, then one sentence reason.

Title: {title}
Body: {body}
"""
    
    @staticmethod
    def generate_caption(description: str, platform: str) -> str:
        return f"""
You are a social media expert. Write an optimized caption for {platform}.

Content description: {description}

Rules:
- Engaging and platform-appropriate
- Include relevant hashtags
- Max 300 characters for Twitter, longer for others

Return only the caption, nothing else.
"""