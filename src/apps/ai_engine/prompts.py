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
    
    @staticmethod
    def adapt_for_platform(content: str, target_platform: str) -> str:
        formats = {
            'instagram': "engaging Instagram caption with emojis and hashtags, max 2200 characters",
            'linkedin': "professional LinkedIn post with insights and a call to action, max 3000 characters",
            'twitter': "punchy X (Twitter) thread, 3-5 tweets, each under 280 characters, numbered 1/, 2/, etc.",
            'youtube': "compelling YouTube video script outline with hook, main points, and CTA",
        }
        fmt = formats.get(target_platform.lower(), "social media post")
        return f"""
    You are a content adaptation expert. Convert the following content into a {fmt}.

    Original Content:
    {content}

    Return only the adapted content, nothing else.
    """

    @staticmethod
    def generate_hashtags(title: str, body: str, platform: str) -> str:
        return f"""
    You are an SEO and social media expert. Generate hashtags and SEO tags for the following content.

    Title: {title}
    Content: {body}
    Platform: {platform}

    Return in this exact format:
    HASHTAGS: #tag1 #tag2 #tag3 #tag4 #tag5
    SEO_TAGS: tag1, tag2, tag3, tag4, tag5
    """