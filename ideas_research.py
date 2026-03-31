import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime

class ValueInvestorsClubResearch:
    """ValueInvestorsClub Ideas와 Topics 리서치 도구"""
    
    BASE_URL = "https://www.valueinvestorsclub.com"
    
    @staticmethod
    def get_latest_ideas(limit=10):
        """최신 Ideas 가져오기"""
        try:
            url = f"{ValueInvestorsClubResearch.BASE_URL}/ideas"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            ideas = []
            # Ideas 데이터 파싱 (구조에 따라 조정 필요)
            idea_elements = soup.find_all('div', class_='idea-item', limit=limit)
            
            for idea in idea_elements:
                try:
                    title = idea.find('h3')
                    author = idea.find('span', class_='author')
                    date = idea.find('span', class_='date')
                    description = idea.find('p', class_='description')
                    
                    ideas.append({
                        'title': title.text if title else 'N/A',
                        'author': author.text if author else 'N/A',
                        'date': date.text if date else 'N/A',
                        'description': description.text if description else 'N/A'
                    })
                except:
                    continue
            
            return json.dumps({
                'source': 'ValueInvestorsClub',
                'type': 'latest_ideas',
                'count': len(ideas),
                'timestamp': datetime.now().isoformat(),
                'ideas': ideas
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_popular_topics(limit=10):
        """인기 있는 Topics 가져오기"""
        try:
            url = f"{ValueInvestorsClubResearch.BASE_URL}/topics"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            topics = []
            # Topics 데이터 파싱 (구조에 따라 조정 필요)
            topic_elements = soup.find_all('div', class_='topic-item', limit=limit)
            
            for topic in topic_elements:
                try:
                    name = topic.find('h4')
                    discussion_count = topic.find('span', class_='discussion-count')
                    latest_post = topic.find('span', class_='latest-post')
                    
                    topics.append({
                        'name': name.text if name else 'N/A',
                        'discussions': discussion_count.text if discussion_count else 'N/A',
                        'latest_post': latest_post.text if latest_post else 'N/A'
                    })
                except:
                    continue
            
            return json.dumps({
                'source': 'ValueInvestorsClub',
                'type': 'popular_topics',
                'count': len(topics),
                'timestamp': datetime.now().isoformat(),
                'topics': topics
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def search_ideas(keyword):
        """특정 키워드로 Ideas 검색"""
        try:
            url = f"{ValueInvestorsClubResearch.BASE_URL}/search?q={keyword}&type=ideas"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return json.dumps({
                'keyword': keyword,
                'source': 'ValueInvestorsClub',
                'url': url,
                'status': 'search_completed'
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def search_topics(keyword):
        """특정 키워드로 Topics 검색"""
        try:
            url = f"{ValueInvestorsClubResearch.BASE_URL}/search?q={keyword}&type=topics"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return json.dumps({
                'keyword': keyword,
                'source': 'ValueInvestorsClub',
                'url': url,
                'status': 'search_completed'
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
    
    @staticmethod
    def get_idea_details(idea_id):
        """특정 Idea의 상세 정보 가져오기"""
        try:
            url = f"{ValueInvestorsClubResearch.BASE_URL}/idea/{idea_id}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            return json.dumps({
                'idea_id': idea_id,
                'url': url,
                'status': 'found'
            }, ensure_ascii=False, indent=2)
        except Exception as e:
            return json.dumps({'error': str(e)}, ensure_ascii=False)
