"""
Gemini AI와의 통합을 위한 모듈
"""

from ideas_research import ValueInvestorsClubResearch
import json

class ValueInvestorsClubGeminiTool:
    """Gemini를 위한 ValueInvestorsClub Ideas & Topics 조회 도구"""
    
    @staticmethod
    def get_latest_ideas_tool():
        """최신 Ideas 조회 Tool 정의"""
        return {
            "name": "get_latest_ideas",
            "description": "ValueInvestorsClub에서 최신 investment ideas를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "조회할 최대 ideas 개수 (기본값: 10)"
                    }
                }
            }
        }
    
    @staticmethod
    def get_popular_topics_tool():
        """인기 Topics 조회 Tool 정의"""
        return {
            "name": "get_popular_topics",
            "description": "ValueInvestorsClub에서 인기 있는 discussion topics를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "조회할 최대 topics 개수 (기본값: 10)"
                    }
                }
            }
        }
    
    @staticmethod
    def search_ideas_tool():
        """Ideas 검색 Tool 정의"""
        return {
            "name": "search_ideas",
            "description": "ValueInvestorsClub에서 특정 키워드로 investment ideas를 검색합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "검색 키워드 (예: Apple, Technology, Dividend 등)"
                    }
                },
                "required": ["keyword"]
            }
        }
    
    @staticmethod
    def search_topics_tool():
        """Topics 검색 Tool 정의"""
        return {
            "name": "search_topics",
            "description": "ValueInvestorsClub에서 특정 키워드로 discussion topics를 검색합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "검색 키워드 (예: Stock Analysis, Portfolio, Market 등)"
                    }
                },
                "required": ["keyword"]
            }
        }
    
    @staticmethod
    def get_idea_details_tool():
        """Idea 상세 정보 조회 Tool 정의"""
        return {
            "name": "get_idea_details",
            "description": "ValueInvestorsClub에서 특정 idea의 상세 정보를 조회합니다.",
            "parameters": {
                "type": "object",
                "properties": {
                    "idea_id": {
                        "type": "string",
                        "description": "Idea ID"
                    }
                },
                "required": ["idea_id"]
            }
        }
    
    @staticmethod
    def execute_get_latest_ideas(limit=10) -> str:
        """최신 Ideas 조회 실행"""
        return ValueInvestorsClubResearch.get_latest_ideas(limit)
    
    @staticmethod
    def execute_get_popular_topics(limit=10) -> str:
        """인기 Topics 조회 실행"""
        return ValueInvestorsClubResearch.get_popular_topics(limit)
    
    @staticmethod
    def execute_search_ideas(keyword: str) -> str:
        """Ideas 검색 실행"""
        return ValueInvestorsClubResearch.search_ideas(keyword)
    
    @staticmethod
    def execute_search_topics(keyword: str) -> str:
        """Topics 검색 실행"""
        return ValueInvestorsClubResearch.search_topics(keyword)
    
    @staticmethod
    def execute_get_idea_details(idea_id: str) -> str:
        """Idea 상세 정보 조회 실행"""
        return ValueInvestorsClubResearch.get_idea_details(idea_id)
