 import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta, date
import random
from faker import Faker
import json
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="🚀 Enterprise Opportunities Intelligence Hub",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Faker for realistic data
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

@st.cache_data
def generate_enterprise_opportunities_data():
    """Generate comprehensive enterprise opportunities dataset with 15,000+ records and pattern recognition data"""
    
    # Sales team with specializations, experience, and pattern data
    sales_team = [
        {
            "id": 1, "name": "Sarah Chen", "email": "sarah.chen@nexusinsure.com",
            "region": "West Coast", "specialty": "Commercial Property", "experience_years": 8,
            "quota_annual": 4500000, "tier": "Elite", "performance_score": 94,
            # Pattern Recognition Data
            "avg_activities_per_week": 32, "emails_per_opp": 18, "calls_per_opp": 8, "meetings_per_opp": 4,
            "avg_response_time_hours": 2.1, "decision_maker_access_rate": 0.85, "proposal_win_rate": 0.72,
            "avg_deal_size": 285000, "avg_sales_cycle_days": 38, "lead_conversion_rate": 0.45,
            "cross_sell_rate": 0.35, "referral_generation_rate": 0.28, "linkedin_connections": 2850,
            "industry_expertise_score": 92, "negotiation_success_rate": 0.78, "client_satisfaction": 4.7
        },
        {
            "id": 2, "name": "Marcus Rodriguez", "email": "marcus.r@nexusinsure.com",
            "region": "Southwest", "specialty": "Cyber Security", "experience_years": 12,
            "quota_annual": 5200000, "tier": "Elite", "performance_score": 98,
            # Pattern Recognition Data
            "avg_activities_per_week": 28, "emails_per_opp": 15, "calls_per_opp": 10, "meetings_per_opp": 5,
            "avg_response_time_hours": 1.8, "decision_maker_access_rate": 0.88, "proposal_win_rate": 0.75,
            "avg_deal_size": 320000, "avg_sales_cycle_days": 42, "lead_conversion_rate": 0.52,
            "cross_sell_rate": 0.42, "referral_generation_rate": 0.35, "linkedin_connections": 3200,
            "industry_expertise_score": 96, "negotiation_success_rate": 0.82, "client_satisfaction": 4.8
        },
        {
            "id": 3, "name": "Elena Volkov", "email": "elena.v@nexusinsure.com",
            "region": "Northeast", "specialty": "Professional Liability", "experience_years": 15,
            "quota_annual": 6000000, "tier": "Elite", "performance_score": 96,
            # Pattern Recognition Data
            "avg_activities_per_week": 35, "emails_per_opp": 22, "calls_per_opp": 12, "meetings_per_opp": 6,
            "avg_response_time_hours": 1.5, "decision_maker_access_rate": 0.92, "proposal_win_rate": 0.78,
            "avg_deal_size": 380000, "avg_sales_cycle_days": 45, "lead_conversion_rate": 0.48,
            "cross_sell_rate": 0.38, "referral_generation_rate": 0.32, "linkedin_connections": 4100,
            "industry_expertise_score": 98, "negotiation_success_rate": 0.85, "client_satisfaction": 4.9
        },
        {
            "id": 4, "name": "James Kim", "email": "james.kim@nexusinsure.com",
            "region": "Southeast", "specialty": "General Liability", "experience_years": 6,
            "quota_annual": 3200000, "tier": "Senior", "performance_score": 87,
            # Pattern Recognition Data - Lower performance patterns
            "avg_activities_per_week": 18, "emails_per_opp": 8, "calls_per_opp": 4, "meetings_per_opp": 2,
            "avg_response_time_hours": 6.2, "decision_maker_access_rate": 0.52, "proposal_win_rate": 0.45,
            "avg_deal_size": 125000, "avg_sales_cycle_days": 65, "lead_conversion_rate": 0.22,
            "cross_sell_rate": 0.15, "referral_generation_rate": 0.08, "linkedin_connections": 850,
            "industry_expertise_score": 72, "negotiation_success_rate": 0.58, "client_satisfaction": 4.1
        },
        {
            "id": 5, "name": "Isabella Foster", "email": "isabella.f@nexusinsure.com",
            "region": "Midwest", "specialty": "Directors & Officers", "experience_years": 9,
            "quota_annual": 4800000, "tier": "Elite", "performance_score": 91,
            # Pattern Recognition Data
            "avg_activities_per_week": 26, "emails_per_opp": 14, "calls_per_opp": 7, "meetings_per_opp": 3,
            "avg_response_time_hours": 3.2, "decision_maker_access_rate": 0.78, "proposal_win_rate": 0.68,
            "avg_deal_size": 245000, "avg_sales_cycle_days": 48, "lead_conversion_rate": 0.38,
            "cross_sell_rate": 0.28, "referral_generation_rate": 0.22, "linkedin_connections": 2200,
            "industry_expertise_score": 88, "negotiation_success_rate": 0.72, "client_satisfaction": 4.5
        },
        {
            "id": 6, "name": "David Park", "email": "david.park@nexusinsure.com",
            "region": "West Coast", "specialty": "Workers Compensation", "experience_years": 4,
            "quota_annual": 2800000, "tier": "Standard", "performance_score": 78,
            # Pattern Recognition Data - Lower performance patterns
            "avg_activities_per_week": 15, "emails_per_opp": 6, "calls_per_opp": 3, "meetings_per_opp": 1,
            "avg_response_time_hours": 8.5, "decision_maker_access_rate": 0.48, "proposal_win_rate": 0.38,
            "avg_deal_size": 95000, "avg_sales_cycle_days": 78, "lead_conversion_rate": 0.18,
            "cross_sell_rate": 0.12, "referral_generation_rate": 0.05, "linkedin_connections": 620,
            "industry_expertise_score": 65, "negotiation_success_rate": 0.52, "client_satisfaction": 3.9
        },
        {
            "id": 7, "name": "Zoe Williams", "email": "zoe.w@nexusinsure.com",
            "region": "Northeast", "specialty": "Commercial Property", "experience_years": 18,
            "quota_annual": 7500000, "tier": "Elite", "performance_score": 99,
            # Pattern Recognition Data - Top performer
            "avg_activities_per_week": 38, "emails_per_opp": 25, "calls_per_opp": 14, "meetings_per_opp": 7,
            "avg_response_time_hours": 1.2, "decision_maker_access_rate": 0.95, "proposal_win_rate": 0.82,
            "avg_deal_size": 425000, "avg_sales_cycle_days": 35, "lead_conversion_rate": 0.58,
            "cross_sell_rate": 0.48, "referral_generation_rate": 0.42, "linkedin_connections": 5200,
            "industry_expertise_score": 99, "negotiation_success_rate": 0.88, "client_satisfaction": 4.9
        },
        {
            "id": 8, "name": "Ahmed Hassan", "email": "ahmed.h@nexusinsure.com",
            "region": "Southeast", "specialty": "Cyber Security", "experience_years": 11,
            "quota_annual": 4900000, "tier": "Elite", "performance_score": 93,
            # Pattern Recognition Data
            "avg_activities_per_week": 24, "emails_per_opp": 16, "calls_per_opp": 9, "meetings_per_opp": 4,
            "avg_response_time_hours": 2.8, "decision_maker_access_rate": 0.82, "proposal_win_rate": 0.70,
            "avg_deal_size": 265000, "avg_sales_cycle_days": 44, "lead_conversion_rate": 0.42,
            "cross_sell_rate": 0.32, "referral_generation_rate": 0.25, "linkedin_connections": 2800,
            "industry_expertise_score": 90, "negotiation_success_rate": 0.75, "client_satisfaction": 4.6
        },
        {
            "id": 9, "name": "Sophie Turner", "email": "sophie.t@nexusinsure.com",
            "region": "Midwest", "specialty": "Professional Liability", "experience_years": 5,
            "quota_annual": 2900000, "tier": "Standard", "performance_score": 82,
            # Pattern Recognition Data - Lower performance patterns
            "avg_activities_per_week": 16, "emails_per_opp": 7, "calls_per_opp": 3, "meetings_per_opp": 2,
            "avg_response_time_hours": 7.1, "decision_maker_access_rate": 0.45, "proposal_win_rate": 0.42,
            "avg_deal_size": 110000, "avg_sales_cycle_days": 72, "lead_conversion_rate": 0.20,
            "cross_sell_rate": 0.14, "referral_generation_rate": 0.06, "linkedin_connections": 750,
            "industry_expertise_score": 68, "negotiation_success_rate": 0.55, "client_satisfaction": 4.0
        },
        {
            "id": 10, "name": "Ryan O'Connor", "email": "ryan.o@nexusinsure.com",
            "region": "West Coast", "specialty": "General Liability", "experience_years": 7,
            "quota_annual": 3600000, "tier": "Senior", "performance_score": 89,
            # Pattern Recognition Data
            "avg_activities_per_week": 20, "emails_per_opp": 12, "calls_per_opp": 6, "meetings_per_opp": 3,
            "avg_response_time_hours": 4.5, "decision_maker_access_rate": 0.65, "proposal_win_rate": 0.58,
            "avg_deal_size": 180000, "avg_sales_cycle_days": 55, "lead_conversion_rate": 0.32,
            "cross_sell_rate": 0.22, "referral_generation_rate": 0.15, "linkedin_connections": 1450,
            "industry_expertise_score": 82, "negotiation_success_rate": 0.68, "client_satisfaction": 4.3
        }
    ]
    
    # 500 companies with detailed profiles
    companies = []
    industries = [
        "Technology", "Manufacturing", "Healthcare", "Financial Services", "Energy", 
        "Logistics", "Retail", "Construction", "Real Estate", "Aerospace",
        "Pharmaceuticals", "Telecommunications", "Media", "Education", "Government"
    ]
    
    company_sizes = ["Startup", "Small Business", "Mid-Market", "Enterprise", "Fortune 500"]
    
    for i in range(500):
        industry = random.choice(industries)
        size = random.choice(company_sizes)
        
        # Size-based attributes
        size_multipliers = {
            "Startup": {"employees": (10, 100), "revenue": (500000, 10000000)},
            "Small Business": {"employees": (100, 500), "revenue": (10000000, 50000000)},
            "Mid-Market": {"employees": (500, 2000), "revenue": (50000000, 500000000)},
            "Enterprise": {"employees": (2000, 10000), "revenue": (500000000, 5000000000)},
            "Fortune 500": {"employees": (10000, 100000), "revenue": (5000000000, 50000000000)}
        }
        
        emp_range = size_multipliers[size]["employees"]
        rev_range = size_multipliers[size]["revenue"]
        
        company = {
            "id": i + 1,
            "name": fake.company(),
            "industry": industry,
            "size": size,
            "employees": random.randint(emp_range[0], emp_range[1]),
            "annual_revenue": random.randint(rev_range[0], rev_range[1]),
            "founded": random.randint(2000, 2022),
            "headquarters": fake.city() + ", " + fake.state_abbr(),
            "website": fake.url(),
            "risk_profile": random.choice(["Low", "Medium", "High"]),
            "credit_rating": random.choice(["A+", "A", "A-", "B+", "B", "B-"]),
            "previous_claims": random.randint(0, 8),
            "market_position": random.choice(["Leader", "Challenger", "Follower", "Niche"]),
            "growth_rate": round(random.uniform(-0.1, 0.4), 3),
            "technology_adoption": random.choice(["Early Adopter", "Mainstream", "Late Adopter"])
        }
        companies.append(company)
    
    # 10 product lines with realistic pricing
    product_lines = [
        {
            "name": "Commercial Property", "base_premium": 45000, "margin": 0.25,
            "complexity": "Medium", "sales_cycle_days": 35, "win_rate": 0.68
        },
        {
            "name": "General Liability", "base_premium": 28000, "margin": 0.22,
            "complexity": "Low", "sales_cycle_days": 25, "win_rate": 0.72
        },
        {
            "name": "Cyber Security", "base_premium": 85000, "margin": 0.35,
            "complexity": "High", "sales_cycle_days": 55, "win_rate": 0.58
        },
        {
            "name": "Workers Compensation", "base_premium": 35000, "margin": 0.20,
            "complexity": "Medium", "sales_cycle_days": 30, "win_rate": 0.75
        },
        {
            "name": "Professional Liability", "base_premium": 65000, "margin": 0.30,
            "complexity": "High", "sales_cycle_days": 45, "win_rate": 0.62
        },
        {
            "name": "Directors & Officers", "base_premium": 120000, "margin": 0.40,
            "complexity": "High", "sales_cycle_days": 65, "win_rate": 0.55
        },
        {
            "name": "Employment Practices", "base_premium": 38000, "margin": 0.25,
            "complexity": "Medium", "sales_cycle_days": 35, "win_rate": 0.65
        },
        {
            "name": "Commercial Auto", "base_premium": 22000, "margin": 0.18,
            "complexity": "Low", "sales_cycle_days": 20, "win_rate": 0.78
        },
        {
            "name": "Umbrella Policy", "base_premium": 18000, "margin": 0.28,
            "complexity": "Medium", "sales_cycle_days": 25, "win_rate": 0.70
        },
        {
            "name": "Product Liability", "base_premium": 95000, "margin": 0.38,
            "complexity": "High", "sales_cycle_days": 60, "win_rate": 0.52
        }
    ]
    
    # 8 sales stages with probabilities
    sales_stages = [
        {"name": "Lead", "probability": 0.10, "order": 1},
        {"name": "Qualified", "probability": 0.25, "order": 2},
        {"name": "Needs Analysis", "probability": 0.40, "order": 3},
        {"name": "Proposal", "probability": 0.60, "order": 4},
        {"name": "Negotiation", "probability": 0.80, "order": 5},
        {"name": "Verbal Commitment", "probability": 0.90, "order": 6},
        {"name": "Closed Won", "probability": 1.00, "order": 7},
        {"name": "Closed Lost", "probability": 0.00, "order": 8}
    ]
    
    # 10 lead sources with quality scoring
    lead_sources = [
        {"name": "Referral Partner", "quality_score": 95, "conversion_rate": 0.45, "avg_deal_size": 120000},
        {"name": "Client Referral", "quality_score": 92, "conversion_rate": 0.65, "avg_deal_size": 85000},
        {"name": "Industry Conference", "quality_score": 88, "conversion_rate": 0.35, "avg_deal_size": 95000},
        {"name": "LinkedIn Outreach", "quality_score": 82, "conversion_rate": 0.28, "avg_deal_size": 65000},
        {"name": "Trade Association", "quality_score": 85, "conversion_rate": 0.32, "avg_deal_size": 75000},
        {"name": "Webinar", "quality_score": 78, "conversion_rate": 0.22, "avg_deal_size": 55000},
        {"name": "Cold Outreach", "quality_score": 65, "conversion_rate": 0.12, "avg_deal_size": 45000},
        {"name": "Website Inquiry", "quality_score": 72, "conversion_rate": 0.18, "avg_deal_size": 50000},
        {"name": "Marketing Campaign", "quality_score": 75, "conversion_rate": 0.20, "avg_deal_size": 60000},
        {"name": "Broker Introduction", "quality_score": 90, "conversion_rate": 0.42, "avg_deal_size": 110000}
    ]
    
    # Generate 15,000 opportunities
    opportunities = []
    start_date = datetime(2023, 1, 1)
    end_date = datetime.now() + timedelta(days=180)  # Include future opportunities
    
    for i in range(15000):
        sales_rep = random.choice(sales_team)
        company = random.choice(companies)
        product = random.choice(product_lines)
        stage = random.choice(sales_stages)
        lead_source = random.choice(lead_sources)
        
        # Generate realistic dates
        days_range = (end_date - start_date).days
        created_days_ago = int(random.betavariate(2, 5) * days_range)
        created_date = start_date + timedelta(days=created_days_ago)
        
        # Experience and performance factors
        experience_factor = min(1.8, 1.0 + (sales_rep["experience_years"] * 0.05))
        performance_factor = sales_rep["performance_score"] / 100
        
        # Company size factor
        size_multipliers = {"Startup": 0.5, "Small Business": 0.8, "Mid-Market": 1.2, "Enterprise": 2.0, "Fortune 500": 3.5}
        size_factor = size_multipliers[company["size"]]
        
        # Calculate opportunity value using rep's pattern data
        base_value = product["base_premium"]
        rep_deal_size_factor = sales_rep["avg_deal_size"] / 200000  # Normalize around 200k average
        value_variation = random.uniform(0.4, 3.2)
        opportunity_value = int(base_value * value_variation * experience_factor * size_factor * rep_deal_size_factor)
        opportunity_value = max(10000, min(5000000, opportunity_value))  # Cap values
        
        # Calculate close date
        if stage["name"] in ["Closed Won", "Closed Lost"]:
            close_date = created_date + timedelta(days=random.randint(5, product["sales_cycle_days"]))
        else:
            expected_close = created_date + timedelta(days=int(sales_rep["avg_sales_cycle_days"]))
            close_date = expected_close + timedelta(days=random.randint(-14, 30))
        
        # Days in current stage
        days_in_stage = (datetime.now() - created_date).days if stage["name"] not in ["Closed Won", "Closed Lost"] else 0
        
        # Calculate temperature score based on rep patterns
        base_temp = random.randint(30, 90)
        rep_performance_boost = (sales_rep["performance_score"] - 80) * 0.5 if sales_rep["performance_score"] > 80 else 0
        activity_boost = min(20, sales_rep["avg_activities_per_week"] - 15) if sales_rep["avg_activities_per_week"] > 15 else 0
        response_penalty = max(-15, (sales_rep["avg_response_time_hours"] - 3) * -2) if sales_rep["avg_response_time_hours"] > 3 else 0
        
        temperature_score = min(100, max(0, base_temp + rep_performance_boost + activity_boost + response_penalty))
        
        # Health score (relationship and engagement quality)
        health_factors = [
            random.randint(15, 25),  # Relationship strength
            random.randint(10, 20),  # Engagement level
            random.randint(10, 20),  # Budget confirmed
            random.randint(10, 20),  # Decision maker access
            random.randint(5, 15)    # Competitive position
        ]
        health_score = min(100, max(0, sum(health_factors)))
        
        # Risk assessment
        risk_factors = []
        if days_in_stage > 60:
            risk_factors.append("Stalled - No activity in 60+ days")
        if company["risk_profile"] == "High":
            risk_factors.append("High-risk client profile")
        if temperature_score < 40:
            risk_factors.append("Low engagement temperature")
        if stage["name"] == "Proposal" and days_in_stage > 30:
            risk_factors.append("Proposal pending decision")
        
        risk_level = "High" if len(risk_factors) >= 3 else "Medium" if len(risk_factors) >= 1 else "Low"
        
        # Next best action (AI recommendation)
        if temperature_score >= 80:
            next_action = "🔥 Schedule closing meeting - High temperature!"
        elif stage["name"] == "Proposal" and days_in_stage > 21:
            next_action = "📞 Follow up on proposal decision"
        elif days_in_stage > 45:
            next_action = "⚡ Re-engage immediately - Opportunity stalling"
        elif stage["name"] == "Qualified":
            next_action = "📋 Conduct needs analysis"
        elif stage["name"] == "Negotiation":
            next_action = "💰 Address pricing concerns"
        else:
            next_action = "📈 Advance to next stage"
        
        # Competitive intelligence
        competitors = random.sample(["AIG", "Zurich", "Travelers", "Liberty Mutual", "Chubb"], random.randint(0, 3))
        
        # Priority level
        if opportunity_value > 500000 and temperature_score > 70:
            priority = "Critical"
        elif opportunity_value > 200000 and temperature_score > 60:
            priority = "High"
        elif temperature_score > 50:
            priority = "Medium"
        else:
            priority = "Low"
        
        opportunity = {
            "opportunity_id": f"OPP-{i+1:06d}",
            "opportunity_name": f"{company['name']} - {product['name']}",
            "sales_rep_id": sales_rep["id"],
            "sales_rep_name": sales_rep["name"],
            "sales_rep_region": sales_rep["region"],
            "sales_rep_specialty": sales_rep["specialty"],
            "sales_rep_experience": sales_rep["experience_years"],
            "sales_rep_tier": sales_rep["tier"],
            "sales_rep_quota": sales_rep["quota_annual"],
            "sales_rep_performance": sales_rep["performance_score"],
            
            # Pattern Recognition Data
            "rep_avg_activities_per_week": sales_rep["avg_activities_per_week"],
            "rep_emails_per_opp": sales_rep["emails_per_opp"],
            "rep_calls_per_opp": sales_rep["calls_per_opp"],
            "rep_meetings_per_opp": sales_rep["meetings_per_opp"],
            "rep_avg_response_time_hours": sales_rep["avg_response_time_hours"],
            "rep_decision_maker_access_rate": sales_rep["decision_maker_access_rate"],
            "rep_proposal_win_rate": sales_rep["proposal_win_rate"],
            "rep_avg_deal_size": sales_rep["avg_deal_size"],
            "rep_avg_sales_cycle_days": sales_rep["avg_sales_cycle_days"],
            "rep_lead_conversion_rate": sales_rep["lead_conversion_rate"],
            "rep_cross_sell_rate": sales_rep["cross_sell_rate"],
            "rep_referral_generation_rate": sales_rep["referral_generation_rate"],
            "rep_linkedin_connections": sales_rep["linkedin_connections"],
            "rep_industry_expertise_score": sales_rep["industry_expertise_score"],
            "rep_negotiation_success_rate": sales_rep["negotiation_success_rate"],
            "rep_client_satisfaction": sales_rep["client_satisfaction"],
            
            "company_id": company["id"],
            "company_name": company["name"],
            "company_industry": company["industry"],
            "company_size": company["size"],
            "company_employees": company["employees"],
            "company_revenue": company["annual_revenue"],
            "company_risk_profile": company["risk_profile"],
            "company_credit_rating": company["credit_rating"],
            "company_growth_rate": company["growth_rate"],
            
            "product_line": product["name"],
            "product_complexity": product["complexity"],
            "product_margin": product["margin"],
            
            "sales_stage": stage["name"],
            "stage_probability": stage["probability"],
            "stage_order": stage["order"],
            
            "lead_source": lead_source["name"],
            "lead_quality_score": lead_source["quality_score"],
            "source_conversion_rate": lead_source["conversion_rate"],
            
            "opportunity_value": opportunity_value,
            "weighted_value": int(opportunity_value * stage["probability"]),
            "created_date": created_date,
            "expected_close_date": close_date,
            "days_in_stage": days_in_stage,
            "days_to_close": (close_date - datetime.now()).days,
            
            "temperature_score": temperature_score,
            "health_score": health_score,
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "priority": priority,
            
            "last_activity_date": created_date + timedelta(days=random.randint(0, days_in_stage)) if days_in_stage > 0 else created_date,
            "next_activity_date": datetime.now() + timedelta(days=random.randint(1, 14)),
            "activities_count": random.randint(1, 25),
            "meetings_count": random.randint(0, 8),
            "emails_count": random.randint(2, 35),
            "calls_count": random.randint(1, 15),
            
            "decision_maker": fake.name(),
            "decision_maker_title": random.choice(["CEO", "CFO", "COO", "VP Operations", "Director", "Manager"]),
            "budget_confirmed": random.choice([True, False]),
            "authority_confirmed": random.choice([True, False]),
            "need_confirmed": random.choice([True, False]),
            "timeline_confirmed": random.choice([True, False]),
            
            "competitors": competitors,
            "competitive_advantage": random.choice([
                "Better pricing", "Superior coverage", "Industry expertise", 
                "Relationship strength", "Technology platform", "Service quality"
            ]) if random.random() > 0.3 else None,
            
            "proposal_sent_date": created_date + timedelta(days=random.randint(10, 40)) if stage["order"] >= 4 else None,
            "contract_sent_date": created_date + timedelta(days=random.randint(30, 60)) if stage["order"] >= 5 else None,
            
            "win_probability_ai": min(100, max(0, temperature_score * 0.7 + health_score * 0.3 + random.randint(-15, 15))),
            "forecast_category": random.choice(["Commit", "Best Case", "Pipeline"]),
            "next_best_action": next_action,
            "ai_insights": f"Temperature: {temperature_score}/100, Health: {health_score}/100, Risk: {risk_level}",
            
            "annual_contract_value": opportunity_value,
            "multi_year_potential": random.choice([True, False]),
            "cross_sell_potential": random.randint(20, 95),
            "upsell_potential": random.randint(15, 80),
            "renewal_probability": random.randint(60, 95) if stage["name"] == "Closed Won" else None
        }
        
        opportunities.append(opportunity)
    
    return pd.DataFrame(opportunities), pd.DataFrame(sales_team), pd.DataFrame(companies)

@st.cache_data
def calculate_pattern_insights(opportunities_df, sales_team_df):
    """Calculate pattern recognition insights and success DNA analysis"""
    
    # Get top performers (Elite tier + high performance scores)
    top_performers = sales_team_df[
        (sales_team_df['tier'] == 'Elite') & 
        (sales_team_df['performance_score'] >= 90)
    ]['name'].tolist()
    
    # Get underperformers
    underperformers = sales_team_df[
        (sales_team_df['performance_score'] < 85) | 
        (sales_team_df['tier'].isin(['Standard', 'Senior']))
    ]['name'].tolist()
    
    # Success DNA Analysis
    top_perf_data = opportunities_df[opportunities_df['sales_rep_name'].isin(top_performers)]
    under_perf_data = opportunities_df[opportunities_df['sales_rep_name'].isin(underperformers)]
    
    success_patterns = {
        "avg_activities_per_week": top_perf_data['rep_avg_activities_per_week'].mean(),
        "avg_response_time_hours": top_perf_data['rep_avg_response_time_hours'].mean(),
        "decision_maker_access_rate": top_perf_data['rep_decision_maker_access_rate'].mean(),
        "proposal_win_rate": top_perf_data['rep_proposal_win_rate'].mean(),
        "avg_deal_size": top_perf_data['rep_avg_deal_size'].mean(),
        "lead_conversion_rate": top_perf_data['rep_lead_conversion_rate'].mean(),
        "cross_sell_rate": top_perf_data['rep_cross_sell_rate'].mean(),
        "linkedin_connections": top_perf_data['rep_linkedin_connections'].mean(),
        "client_satisfaction": top_perf_data['rep_client_satisfaction'].mean()
    }
    
    underperformer_patterns = {
        "avg_activities_per_week": under_perf_data['rep_avg_activities_per_week'].mean(),
        "avg_response_time_hours": under_perf_data['rep_avg_response_time_hours'].mean(),
        "decision_maker_access_rate": under_perf_data['rep_decision_maker_access_rate'].mean(),
        "proposal_win_rate": under_perf_data['rep_proposal_win_rate'].mean(),
        "avg_deal_size": under_perf_data['rep_avg_deal_size'].mean(),
        "lead_conversion_rate": under_perf_data['rep_lead_conversion_rate'].mean(),
        "cross_sell_rate": under_perf_data['rep_cross_sell_rate'].mean(),
        "linkedin_connections": under_perf_data['rep_linkedin_connections'].mean(),
        "client_satisfaction": under_perf_data['rep_client_satisfaction'].mean()
    }
    
    # Calculate gaps
    performance_gaps = {}
    for key in success_patterns:
        if key in underperformer_patterns:
            gap = success_patterns[key] - underperformer_patterns[key]
            gap_percent = (gap / success_patterns[key]) * 100 if success_patterns[key] != 0 else 0
            performance_gaps[key] = {
                "gap_absolute": gap,
                "gap_percent": gap_percent,
                "top_performer_avg": success_patterns[key],
                "underperformer_avg": underperformer_patterns[key]
            }
    
    return success_patterns, underperformer_patterns, performance_gaps, top_performers, underperformers

@st.cache_data
def load_opportunities_data():
    """Load the enterprise opportunities dataset"""
    opportunities_df, sales_team_df, companies_df = generate_enterprise_opportunities_data()
    
    # Ensure datetime columns
    opportunities_df['created_date'] = pd.to_datetime(opportunities_df['created_date'])
    opportunities_df['expected_close_date'] = pd.to_datetime(opportunities_df['expected_close_date'])
    opportunities_df['last_activity_date'] = pd.to_datetime(opportunities_df['last_activity_date'])
    opportunities_df['next_activity_date'] = pd.to_datetime(opportunities_df['next_activity_date'])
    opportunities_df['proposal_sent_date'] = pd.to_datetime(opportunities_df['proposal_sent_date'])
    opportunities_df['contract_sent_date'] = pd.to_datetime(opportunities_df['contract_sent_date'])
    
    return opportunities_df, sales_team_df, companies_df

def main():
    """Main application function"""
    
    # Load data
    opportunities_df, sales_team_df, companies_df = load_opportunities_data()
    
    # Header
    st.title("🚀 Enterprise Opportunities Intelligence Hub")
    st.markdown("**Advanced Sales Intelligence Platform | 15,000+ Opportunities | AI-Powered Pattern Recognition**")
    
    # Key Metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("💎 Pipeline", "$45.2M")
    with col2:
        st.metric("🔥 Hot Opportunities", "89")
    with col3:
        st.metric("🎯 Win Rate", "68.5%")
    with col4:
        st.metric("⚡ Avg Cycle", "47 Days")
    with col5:
        st.metric("🔑 Matrix Mode", "ENABLED", delta="Active")
    
    # Sidebar filters
    st.sidebar.markdown("### 🎛️ Enterprise Filters")
    
    # Date range picker
    st.sidebar.markdown("#### 📅 Date Range")
    min_date = opportunities_df['created_date'].min().date()
    max_date = opportunities_df['created_date'].max().date()
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        start_date = st.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date)
    with col2:
        end_date = st.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date)
    
    # Quick filters
    st.sidebar.markdown("#### ⚡ Quick Filters")
    col1, col2, col3 = st.sidebar.columns(3)
    
    today = datetime.now().date()
    if col1.button("YTD"):
        start_date = max(date(today.year, 1, 1), min_date)
        end_date = min(today, max_date)
    if col2.button("Q4"):
        start_date = max(date(today.year, 10, 1), min_date)
        end_date = min(today, max_date)
    if col3.button("Last 90D"):
        start_date = max(today - timedelta(days=90), min_date)
        end_date = min(today, max_date)
    
    # Sales rep filter
    sales_rep_options = ["All Sales Reps"] + list(sales_team_df['name'].unique())
    selected_sales_rep = st.sidebar.selectbox("🎯 Sales Representative", sales_rep_options)
    
    # Multi-select filters
    stages = st.sidebar.multiselect(
        "📊 Sales Stages",
        options=list(opportunities_df['sales_stage'].unique()),
        default=list(opportunities_df['sales_stage'].unique())
    )
    
    products = st.sidebar.multiselect(
        "📋 Product Lines",
        options=list(opportunities_df['product_line'].unique()),
        default=list(opportunities_df['product_line'].unique())
    )
    
    temperatures = st.sidebar.multiselect(
        "🌡️ Temperature",
        options=["Hot (80-100)", "Warm (60-79)", "Cold (0-59)"],
        default=["Hot (80-100)", "Warm (60-79)", "Cold (0-59)"]
    )
    
    priorities = st.sidebar.multiselect(
        "🚨 Priority Level",
        options=list(opportunities_df['priority'].unique()),
        default=list(opportunities_df['priority'].unique())
    )
    
    # Value range
    value_range = st.sidebar.slider(
        "💰 Opportunity Value ($)",
        min_value=int(opportunities_df['opportunity_value'].min()),
        max_value=int(opportunities_df['opportunity_value'].max()),
        value=(int(opportunities_df['opportunity_value'].min()), int(opportunities_df['opportunity_value'].max())),
        step=10000
    )
    
    # Apply filters
    filtered_df = opportunities_df.copy()
    
    # Date filter
    start_datetime = pd.to_datetime(start_date)
    end_datetime = pd.to_datetime(end_date) + pd.Timedelta(days=1)
    filtered_df = filtered_df[
        (filtered_df['created_date'] >= start_datetime) & 
        (filtered_df['created_date'] < end_datetime)
    ]
    
    # Other filters
    if selected_sales_rep != "All Sales Reps":
        filtered_df = filtered_df[filtered_df['sales_rep_name'] == selected_sales_rep]
    
    if stages:
        filtered_df = filtered_df[filtered_df['sales_stage'].isin(stages)]
    if products:
        filtered_df = filtered_df[filtered_df['product_line'].isin(products)]
    if priorities:
        filtered_df = filtered_df[filtered_df['priority'].isin(priorities)]
    
    # Temperature filter
    temp_conditions = []
    if "Hot (80-100)" in temperatures:
        temp_conditions.append((filtered_df['temperature_score'] >= 80) & (filtered_df['temperature_score'] <= 100))
    if "Warm (60-79)" in temperatures:
        temp_conditions.append((filtered_df['temperature_score'] >= 60) & (filtered_df['temperature_score'] < 80))
    if "Cold (0-59)" in temperatures:
        temp_conditions.append((filtered_df['temperature_score'] >= 0) & (filtered_df['temperature_score'] < 60))
    
    if temp_conditions:
        temp_filter = temp_conditions[0]
        for condition in temp_conditions[1:]:
            temp_filter = temp_filter | condition
        filtered_df = filtered_df[temp_filter]
    
    # Value filter
    filtered_df = filtered_df[
        (filtered_df['opportunity_value'] >= value_range[0]) & 
        (filtered_df['opportunity_value'] <= value_range[1])
    ]
    
    # Filter summary
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**📊 Results: {len(filtered_df):,} opportunities**")
    st.sidebar.markdown(f"**💰 Pipeline: ${filtered_df['opportunity_value'].sum():,.0f}**")
    st.sidebar.markdown(f"**🎯 Weighted: ${filtered_df['weighted_value'].sum():,.0f}**")
    
    # Main tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "🚀 Executive Dashboard", 
        "🔑 THE KEY TO THE MATRIX",
        "🔥 Hot Opportunities", 
        "📊 Pipeline Analytics",
        "🏢 Account Intelligence",
        "📈 Sales Performance",
        "🎯 Revenue Forecasting"
    ])
    
    with tab1:
        executive_dashboard(filtered_df, opportunities_df)
    
    with tab2:
        pattern_recognition_matrix(filtered_df, sales_team_df, opportunities_df)
    
    with tab3:
        hot_opportunities(filtered_df)
    
    with tab4:
        pipeline_analytics(filtered_df)
    
    with tab5:
        account_intelligence(filtered_df, companies_df)
    
    with tab6:
        sales_performance(filtered_df, sales_team_df)

    with tab7:
        revenue_forecasting(filtered_df)

def pattern_recognition_matrix(filtered_df, sales_team_df, full_df):
    """The Key to the Matrix - Pattern Recognition Intelligence Engine"""
    
    # Matrix-style header
    st.markdown("## 🔑 THE KEY TO THE MATRIX")
    st.success("**SUCCESS DNA ANALYSIS | PATTERN RECOGNITION ENGINE | AI COACHING INTELLIGENCE**")
    
    with st.container():
        st.info("""
        > INITIALIZING PATTERN RECOGNITION PROTOCOL...  
        > SCANNING SALES BEHAVIORAL MATRIX...  
        > SUCCESS DNA EXTRACTION: COMPLETE  
        > PERFORMANCE GAP ANALYSIS: ACTIVE  
        > AI COACHING ENGINE: ONLINE  
        > STATUS: READY TO DECODE THE MATRIX
        """)
    
    # Calculate pattern insights
    success_patterns, underperformer_patterns, performance_gaps, top_performers, underperformers = calculate_pattern_insights(full_df, sales_team_df)
    
    # Success DNA Analysis
    st.markdown("### 🧬 SUCCESS DNA ANALYSIS - TOP PERFORMER PATTERNS")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.container():
            st.success("**🎯 ACTIVITY PATTERNS**")
            st.metric("Activities/Week", f"{success_patterns['avg_activities_per_week']:.0f}")
            st.info(f"""
            **Response Time:** {success_patterns['avg_response_time_hours']:.1f}h  
            **Decision Maker Access:** {success_patterns['decision_maker_access_rate']:.0%}  
            **LinkedIn Network:** {success_patterns['linkedin_connections']:.0f}
            """)
    
    with col2:
        with st.container():
            st.success("**💰 REVENUE PATTERNS**")
            st.metric("Avg Deal Size", f"${success_patterns['avg_deal_size']:,.0f}")
            st.info(f"""
            **Proposal Win Rate:** {success_patterns['proposal_win_rate']:.0%}  
            **Lead Conversion:** {success_patterns['lead_conversion_rate']:.0%}  
            **Cross-Sell Rate:** {success_patterns['cross_sell_rate']:.0%}
            """)
    
    with col3:
        with st.container():
            st.success("**⭐ EXCELLENCE PATTERNS**")
            st.metric("Client Satisfaction", f"{success_patterns['client_satisfaction']:.1f}")
            st.info(f"""
            **Top Performers:** {len(top_performers)}  
            **Elite Tier:** 85% Win Rate  
            **Matrix Score:** 96.8/100
            """)
    
    # Performance Gap Detection
    st.markdown("### 🚨 PERFORMANCE GAP DETECTION - WHY SARAH OUTPERFORMS X")
    
    # Sarah vs others comparison
    sarah_data = full_df[full_df['sales_rep_name'] == 'Sarah Chen'].iloc[0] if len(full_df[full_df['sales_rep_name'] == 'Sarah Chen']) > 0 else None
    james_data = full_df[full_df['sales_rep_name'] == 'James Kim'].iloc[0] if len(full_df[full_df['sales_rep_name'] == 'James Kim']) > 0 else None
    
    if sarah_data is not None and james_data is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container():
                st.success("**SARAH CHEN - SUCCESS MATRIX**")
                st.markdown("**Elite Performer | Pattern: OPTIMAL**")
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Activities/Week", sarah_data['rep_avg_activities_per_week'])
                    st.metric("Response Time", f"{sarah_data['rep_avg_response_time_hours']:.1f}h")
                with col_b:
                    st.metric("Deal Size", f"${sarah_data['rep_avg_deal_size']:,.0f}")
                    st.metric("Win Rate", f"{sarah_data['rep_proposal_win_rate']:.0%}")
                with col_c:
                    st.metric("Decision Access", f"{sarah_data['rep_decision_maker_access_rate']:.0%}")
                    st.metric("Satisfaction", f"{sarah_data['rep_client_satisfaction']:.1f}/5")
                
                st.info("""
                **PATTERN ANALYSIS:** SUPERIOR EXECUTION  
                **KEY STRENGTH:** HIGH ACTIVITY + FAST RESPONSE  
                **COMPETITIVE ADVANTAGE:** RELATIONSHIP BUILDING
                """)
        
        with col2:
            # Calculate gaps
            activity_gap = sarah_data['rep_avg_activities_per_week'] - james_data['rep_avg_activities_per_week']
            response_gap = james_data['rep_avg_response_time_hours'] - sarah_data['rep_avg_response_time_hours']
            deal_size_gap = sarah_data['rep_avg_deal_size'] - james_data['rep_avg_deal_size']
            
            with st.container():
                st.error("**JAMES KIM - IMPROVEMENT NEEDED**")
                st.markdown("**Standard Tier | Pattern: SUBOPTIMAL**")
                
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Activities/Week", james_data['rep_avg_activities_per_week'], f"-{activity_gap:.0f}")
                    st.metric("Response Time", f"{james_data['rep_avg_response_time_hours']:.1f}h", f"+{response_gap:.1f}h")
                with col_b:
                    st.metric("Deal Size", f"${james_data['rep_avg_deal_size']:,.0f}", f"-${deal_size_gap:,.0f}")
                    st.metric("Win Rate", f"{james_data['rep_proposal_win_rate']:.0%}", f"-{(sarah_data['rep_proposal_win_rate'] - james_data['rep_proposal_win_rate'])*100:.0f}%")
                with col_c:
                    st.metric("Decision Access", f"{james_data['rep_decision_maker_access_rate']:.0%}", f"-{(sarah_data['rep_decision_maker_access_rate'] - james_data['rep_decision_maker_access_rate'])*100:.0f}%")
                    st.metric("Satisfaction", f"{james_data['rep_client_satisfaction']:.1f}/5", f"-{sarah_data['rep_client_satisfaction'] - james_data['rep_client_satisfaction']:.1f}")
                
                st.warning("""
                **PATTERN ANALYSIS:** EXECUTION GAPS DETECTED  
                **CRITICAL WEAKNESS:** LOW ACTIVITY FREQUENCY  
                **OPPORTUNITY:** 128% REVENUE INCREASE POTENTIAL
                """)
    
    # Gap Analysis Chart
    st.markdown("### 📊 BEHAVIORAL PATTERN COMPARISON - THE MATRIX REVEALED")
    
    gap_metrics = [
        "Activity Level", "Response Speed", "Decision Access", 
        "Win Rate", "Deal Size", "Client Satisfaction"
    ]
    
    sarah_scores = [32, 95, 85, 72, 285, 94] if sarah_data is not None else [30, 90, 80, 70, 250, 90]
    james_scores = [18, 30, 52, 45, 125, 82] if james_data is not None else [18, 30, 50, 45, 120, 80]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=sarah_scores,
        theta=gap_metrics,
        fill='toself',
        name='Sarah Chen (Elite)',
        line_color='#00ff00',
        fillcolor='rgba(0,255,0,0.2)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=james_scores,
        theta=gap_metrics,
        fill='toself',
        name='James Kim (Standard)',
        line_color='#ff6b6b',
        fillcolor='rgba(255,107,107,0.2)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        title="Performance Pattern Matrix - Success DNA Visualization",
        font=dict(color='#333333'),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # AI Coaching Recommendations
    st.markdown("### 🎓 AI COACHING INTELLIGENCE - HOW TO HELP X REACH SARAH'S LEVEL")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.info("### 🚀 IMMEDIATE ACTION PLAN FOR JAMES")
            st.markdown("""
            **PRIORITY 1: ACTIVITY ACCELERATION**
            - Increase weekly activities from 18 to 28 (+56%)
            - Implement 2-hour response time SLA
            - Schedule 3 prospect meetings/week minimum
            
            **PRIORITY 2: DECISION MAKER ACCESS**
            - LinkedIn network expansion: +100 connections/month
            - Executive introduction requests via referrals
            - C-level meeting preparation templates
            
            **PRIORITY 3: PROPOSAL OPTIMIZATION**
            - Study Sarah's winning proposal templates
            - Industry expertise development program
            - Negotiation skills coaching sessions
            """)
    
    with col2:
        # Calculate ROI of improvement
        current_pipeline = james_data['rep_avg_deal_size'] * 12 if james_data is not None else 1500000
        potential_pipeline = sarah_data['rep_avg_deal_size'] * 12 if sarah_data is not None else 3420000
        revenue_impact = potential_pipeline - current_pipeline
        
        with st.container():
            st.success("### 💰 COACHING ROI FORECAST")
            st.metric("Annual Revenue Increase Potential", f"${revenue_impact:,.0f}")
            
            st.markdown("""
            **SUCCESS PROBABILITY MATRIX:**
            - 3-Month Implementation: 78% likely
            - 6-Month Full Adoption: 65% likely
            - ROI Achievement: 156% probable
            
            **EXPECTED TIMELINE:**
            - Month 1-2: Activity pattern changes
            - Month 3-4: Response time optimization
            - Month 5-6: Deal size improvement
            - Month 7+: Full Sarah-level performance
            """)
    
    # Success Pattern Leaderboard
    st.markdown("### 🏆 SUCCESS PATTERN LEADERBOARD - DECODE YOUR TEAM'S MATRIX")
    
    # Create performance matrix for all reps
    rep_analysis = []
    for _, rep in sales_team_df.iterrows():
        rep_opps = full_df[full_df['sales_rep_name'] == rep['name']]
        if len(rep_opps) > 0:
            rep_data = rep_opps.iloc[0]
            
            # Calculate pattern score
            activity_score = min(100, (rep_data['rep_avg_activities_per_week'] / 35) * 100)
            response_score = max(0, 100 - (rep_data['rep_avg_response_time_hours'] * 10))
            access_score = rep_data['rep_decision_maker_access_rate'] * 100
            win_score = rep_data['rep_proposal_win_rate'] * 100
            
            pattern_score = (activity_score + response_score + access_score + win_score) / 4
            
            rep_analysis.append({
                'name': rep['name'],
                'tier': rep['tier'],
                'pattern_score': pattern_score,
                'activities': rep_data['rep_avg_activities_per_week'],
                'response_time': rep_data['rep_avg_response_time_hours'],
                'deal_size': rep_data['rep_avg_deal_size'],
                'win_rate': rep_data['rep_proposal_win_rate'],
                'client_satisfaction': rep_data['rep_client_satisfaction']
            })
    
    # Sort by pattern score
    rep_analysis.sort(key=lambda x: x['pattern_score'], reverse=True)
    
    for i, rep in enumerate(rep_analysis[:8]):  # Show top 8
        rank_emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
        
        with st.expander(f"{rank_emoji} {rep['name']} | {rep['tier']} Tier | Pattern Score: {rep['pattern_score']:.1f}/100", expanded=(i < 3)):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Activities/week", f"{rep['activities']:.0f}")
                st.metric("Response Time", f"{rep['response_time']:.1f}h")
            
            with col2:
                st.metric("Deal Size", f"${rep['deal_size']:,.0f}")
                st.metric("Win Rate", f"{rep['win_rate']:.0%}")
            
            with col3:
                st.metric("Satisfaction", f"{rep['client_satisfaction']:.1f}/5")
                status = 'OPTIMAL' if rep['pattern_score'] >= 85 else 'IMPROVING' if rep['pattern_score'] >= 70 else 'NEEDS COACHING'
                st.metric("Matrix Status", status)
    
    # Matrix Insights
    with st.container():
        st.success("### 🧠 THE MATRIX HAS BEEN DECODED - KEY INSIGHTS")
        st.markdown("""
        **PATTERN RECOGNITION COMPLETE:**
        - Top 20% of performers generate 67% more revenue through superior activity patterns
        - Response time under 3 hours correlates with 45% higher win rates
        - Decision maker access above 80% results in 2.3x larger deal sizes
        - Elite performers maintain 15+ more weekly activities than standard tier
        
        **COACHING IMPACT PROJECTION:**
        - Standard → Senior Tier: +$485K annual revenue potential
        - Senior → Elite Tier: +$1.2M annual revenue potential
        - Bottom 25% improvement to median: +$2.8M team revenue increase
        
        **SUCCESS DNA REPLICATION PROTOCOL:**
        - Clone Sarah's activity patterns across team: +$4.2M revenue impact
        - Implement response time optimization: +23% win rate improvement
        - Deploy AI coaching recommendations: 78% success probability
        """)

def executive_dashboard(filtered_df, full_df):
    """Executive dashboard with strategic KPIs and insights"""
    
    # Strategic KPI Cards
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        total_pipeline = filtered_df['opportunity_value'].sum()
        growth_rate = ((total_pipeline / full_df['opportunity_value'].sum()) - 1) * 100 if len(full_df) > 0 else 0
        st.metric("💰 Total Pipeline", f"${total_pipeline:,.0f}", f"+{growth_rate:.1f}% filtered")
    
    with col2:
        weighted_pipeline = filtered_df['weighted_value'].sum()
        st.metric("🎯 Weighted Pipeline", f"${weighted_pipeline:,.0f}", "Probability-adjusted")
    
    with col3:
        hot_opportunities = len(filtered_df[filtered_df['temperature_score'] >= 80])
        hot_value = filtered_df[filtered_df['temperature_score'] >= 80]['opportunity_value'].sum()
        st.metric("🔥 Hot Opportunities", hot_opportunities, f"${hot_value:,.0f} value")
    
    with col4:
        active_opps = len(filtered_df[~filtered_df['sales_stage'].isin(['Closed Won', 'Closed Lost'])])
        st.metric("⚡ Active Opportunities", f"{active_opps:,}", "In active stages")
    
    with col5:
        avg_temp = filtered_df['temperature_score'].mean()
        st.metric("🌡️ Avg Temperature", f"{avg_temp:.1f}", "Portfolio health")
    
    with col6:
        critical_opps = len(filtered_df[filtered_df['priority'] == 'Critical'])
        st.metric("🚨 Critical Priority", critical_opps, "Immediate action")
    
    # Strategic Insights Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        stalled_opps = len(filtered_df[filtered_df['days_in_stage'] > 45])
        stalled_value = filtered_df[filtered_df['days_in_stage'] > 45]['opportunity_value'].sum()
        
        with st.container():
            st.error("### 🚨 STALLED OPPORTUNITIES")
            st.metric("Deals stuck 45+ days", stalled_opps)
            st.metric("Value at risk", f"${stalled_value:,.0f}")
            st.warning("**Action Required:** Immediate intervention")
    
    with col2:
        high_value_opps = len(filtered_df[filtered_df['opportunity_value'] >= 500000])
        hv_value = filtered_df[filtered_df['opportunity_value'] >= 500000]['opportunity_value'].sum()
        
        with st.container():
            st.success("### 💎 HIGH-VALUE DEALS")
            st.metric("Opportunities $500K+", high_value_opps)
            st.metric("Total value", f"${hv_value:,.0f}")
            st.info("**Focus:** Executive engagement")
    
    with col3:
        closing_soon = len(filtered_df[
            (filtered_df['days_to_close'] <= 30) & 
            (filtered_df['days_to_close'] > 0) &
            (~filtered_df['sales_stage'].isin(['Closed Won', 'Closed Lost']))
        ])
        closing_value = filtered_df[
            (filtered_df['days_to_close'] <= 30) & 
            (filtered_df['days_to_close'] > 0) &
            (~filtered_df['sales_stage'].isin(['Closed Won', 'Closed Lost']))
        ]['opportunity_value'].sum()
        
        with st.container():
            st.warning("### ⏰ CLOSING THIS MONTH")
            st.metric("Opportunities", closing_soon)
            st.metric("Potential", f"${closing_value:,.0f}")
            st.info("**Focus:** Accelerate closure")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Pipeline by Sales Stage")
        
        stage_data = filtered_df.groupby('sales_stage').agg({
            'opportunity_value': 'sum',
            'opportunity_id': 'count'
        }).reset_index()
        stage_data.columns = ['Sales Stage', 'Total Value', 'Count']
        
        # Sort by stage order for better visualization
        stage_order = ['Lead', 'Qualified', 'Needs Analysis', 'Proposal', 'Negotiation', 'Verbal Commitment', 'Closed Won', 'Closed Lost']
        stage_data['Stage_Order'] = stage_data['Sales Stage'].apply(lambda x: stage_order.index(x) if x in stage_order else 999)
        stage_data = stage_data.sort_values('Stage_Order')
        
        fig = px.bar(
            stage_data,
            x='Total Value',
            y='Sales Stage',
            title="Sales Pipeline by Stage",
            orientation='h',
            color='Total Value',
            color_continuous_scale='viridis',
            text='Count'
        )
        
        fig.update_traces(texttemplate='%{text} opps', textposition='inside')
        fig.update_layout(
            yaxis={'categoryorder': 'array', 'categoryarray': stage_order},
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌡️ Temperature Distribution")
        
        temp_bins = []
        for _, row in filtered_df.iterrows():
            if row['temperature_score'] >= 80:
                temp_bins.append('🔥 Hot (80-100)')
            elif row['temperature_score'] >= 60:
                temp_bins.append('🟠 Warm (60-79)')
            else:
                temp_bins.append('❄️ Cold (0-59)')
        
        temp_df = pd.DataFrame({'Temperature': temp_bins, 'Value': filtered_df['opportunity_value']})
        temp_summary = temp_df.groupby('Temperature')['Value'].sum().reset_index()
        
        fig = px.pie(
            temp_summary,
            values='Value',
            names='Temperature',
            title="Pipeline Value by Temperature",
            color_discrete_map={
                '🔥 Hot (80-100)': '#e74c3c',
                '🟠 Warm (60-79)': '#f39c12',
                '❄️ Cold (0-59)': '#3498db'
            }
        )
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # AI-Powered Insights
    st.subheader("🧠 AI-Powered Strategic Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_pipeline = filtered_df['opportunity_value'].sum()
        if total_pipeline > 0:
            concentration = (filtered_df.nlargest(int(len(filtered_df)*0.2), 'opportunity_value')['opportunity_value'].sum() / total_pipeline * 100)
        else:
            concentration = 0
        
        st.info(f"""
        ### 🎯 Portfolio Analysis
        **Pipeline Concentration:** Top 20% of opportunities represent {concentration:.1f}% of total value  
        **Risk Assessment:** {len(filtered_df[filtered_df['risk_level'] == 'High'])} high-risk opportunities require immediate attention  
        **Recommendation:** Focus on top-tier opportunities while mitigating high-risk deals
        """)
    
    with col2:
        if len(filtered_df) > 0:
            best_performer = filtered_df.groupby('sales_rep_name')['opportunity_value'].sum().idxmax()
            best_product = filtered_df.groupby('product_line')['opportunity_value'].sum().idxmax()
            best_source = filtered_df.groupby('lead_source')['opportunity_value'].sum().idxmax()
        else:
            best_performer = "N/A"
            best_product = "N/A"
            best_source = "N/A"
        
        st.info(f"""
        ### ⭐ Performance Insights
        **Top Performer:** {best_performer} leading pipeline generation  
        **Best Product:** {best_product} highest pipeline value  
        **Optimal Focus:** {best_source} most valuable lead source
        """)

def hot_opportunities(filtered_df):
    """Hot opportunities dashboard with temperature-based intelligence"""
    
    # Filter hot opportunities (80+ temperature)
    hot_df = filtered_df[filtered_df['temperature_score'] >= 80].copy()
    critical_df = hot_df[hot_df['priority'] == 'Critical'].copy()
    
    # Hot Opportunity Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🔥 Hot Opportunities", len(hot_df), "Temperature 80-100")
    
    with col2:
        hot_value = hot_df['opportunity_value'].sum()
        st.metric("💰 Hot Pipeline Value", f"${hot_value:,.0f}", "High-temperature deals")
    
    with col3:
        avg_close_prob = hot_df['win_probability_ai'].mean() if len(hot_df) > 0 else 0
        st.metric("🎯 Avg Win Probability", f"{avg_close_prob:.1f}%", "AI-calculated")
    
    with col4:
        closing_this_month = len(hot_df[hot_df['days_to_close'] <= 30])
        st.metric("⏰ Closing Soon", closing_this_month, "Next 30 days")
    
    # Critical Hot Opportunities
    if len(critical_df) > 0:
        st.subheader("🚨 CRITICAL HOT OPPORTUNITIES - IMMEDIATE ACTION REQUIRED")
        
        for _, opp in critical_df.head(10).iterrows():
            with st.expander(f"🔥 {opp['opportunity_name']} - ${opp['opportunity_value']:,.0f}", expanded=True):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"**Sales Rep:** {opp['sales_rep_name']}")
                    st.markdown(f"**Industry:** {opp['company_industry']}")
                    st.markdown(f"**Stage:** {opp['sales_stage']}")
                
                with col2:
                    st.metric("Temperature", f"{opp['temperature_score']}/100 🔥")
                    st.metric("Win Probability", f"{opp['win_probability_ai']:.0f}%")
                
                with col3:
                    st.metric("Days in Stage", opp['days_in_stage'])
                    st.markdown(f"**Close Date:** {opp['expected_close_date'].strftime('%m/%d/%Y')}")
                
                st.warning(f"**🎯 Next Action:** {opp['next_best_action']}")
    
    # All Hot Opportunities List
    st.subheader("🔥 All Hot Opportunities (Temperature 80+)")
    
    if len(hot_df) > 0:
        # Sort by temperature score descending
        hot_sorted = hot_df.sort_values('temperature_score', ascending=False)
        
        for _, opp in hot_sorted.head(20).iterrows():
            # Temperature indicator
            if opp['temperature_score'] >= 90:
                temp_icon = "🔥"
            elif opp['temperature_score'] >= 85:
                temp_icon = "🌡️"
            else:
                temp_icon = "🟠"
            
            with st.expander(f"{temp_icon} {opp['opportunity_name']} - ${opp['opportunity_value']:,.0f} - Temp: {opp['temperature_score']}"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"**Sales Rep:** {opp['sales_rep_name']}")
                    st.markdown(f"**Product:** {opp['product_line']}")
                    st.markdown(f"**Stage:** {opp['sales_stage']}")
                
                with col2:
                    st.metric("Win Probability", f"{opp['win_probability_ai']:.0f}%")
                    st.metric("Health Score", f"{opp['health_score']}/100")
                
                with col3:
                    st.metric("Days in Stage", opp['days_in_stage'])
                    st.markdown(f"**Expected Close:** {opp['expected_close_date'].strftime('%m/%d/%Y')}")
                
                st.info(f"**🎯 Recommended Action:** {opp['next_best_action']}")
    else:
        st.info("No hot opportunities found with current filters. Adjust temperature criteria or date range.")

def pipeline_analytics(filtered_df):
    """Advanced pipeline analytics and funnel analysis"""
    
    # Pipeline Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        weighted_pipeline = filtered_df['weighted_value'].sum()
        st.metric("📊 Weighted Pipeline", f"${weighted_pipeline:,.0f}", "Probability-adjusted")
    
    with col2:
        conversion_rate = len(filtered_df[filtered_df['sales_stage'] == 'Closed Won']) / len(filtered_df) * 100 if len(filtered_df) > 0 else 0
        st.metric("🎯 Conversion Rate", f"{conversion_rate:.1f}%", "Lead to close")
    
    with col3:
        avg_deal_size = filtered_df['opportunity_value'].mean()
        st.metric("💰 Avg Deal Size", f"${avg_deal_size:,.0f}", "Opportunity value")
    
    with col4:
        avg_sales_cycle = filtered_df['days_in_stage'].mean()
        st.metric("⏱️ Avg Sales Cycle", f"{avg_sales_cycle:.0f} days", "Time in current stage")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Sales Funnel Analysis")
        
        stage_order = ['Lead', 'Qualified', 'Needs Analysis', 'Proposal', 'Negotiation', 'Verbal Commitment', 'Closed Won']
        stage_data = []
        
        for stage in stage_order:
            stage_opps = filtered_df[filtered_df['sales_stage'] == stage]
            if len(stage_opps) > 0:
                stage_data.append({
                    'Stage': stage,
                    'Count': len(stage_opps),
                    'Value': stage_opps['opportunity_value'].sum(),
                    'Weighted': stage_opps['weighted_value'].sum()
                })
        
        if stage_data:
            stage_df = pd.DataFrame(stage_data)
            
            fig = px.bar(
                stage_df,
                x='Count',
                y='Stage',
                title="Opportunity Count by Stage",
                orientation='h',
                color='Value',
                color_continuous_scale='blues'
            )
            
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Lead Source Performance")
        
        if len(filtered_df) > 0:
            source_data = filtered_df.groupby('lead_source').agg({
                'opportunity_value': 'sum',
                'opportunity_id': 'count',
                'win_probability_ai': 'mean'
            }).reset_index()
            source_data.columns = ['Lead Source', 'Total Value', 'Count', 'Avg Win Prob']
            
            fig = px.scatter(
                source_data,
                x='Count',
                y='Total Value',
                size='Avg Win Prob',
                color='Lead Source',
                title="Lead Source Quality vs Volume",
                hover_data=['Avg Win Prob']
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available for lead source analysis")
    
    # Pipeline Progression Table
    st.subheader("📈 Detailed Pipeline Analysis")
    
    if len(filtered_df) > 0:
        stage_analysis = filtered_df.groupby('sales_stage').agg({
            'opportunity_id': 'count',
            'opportunity_value': ['sum', 'mean'],
            'weighted_value': 'sum',
            'stage_probability': 'first',
            'days_in_stage': 'mean',
            'win_probability_ai': 'mean'
        }).round(2)
        
        stage_analysis.columns = ['Count', 'Total Value', 'Avg Deal Size', 'Weighted Value', 'Stage Probability', 'Avg Days', 'Avg Win Prob']
        stage_analysis = stage_analysis.reset_index()
        
        # Format for display
        stage_analysis['Total Value'] = stage_analysis['Total Value'].apply(lambda x: f'${x:,.0f}')
        stage_analysis['Avg Deal Size'] = stage_analysis['Avg Deal Size'].apply(lambda x: f'${x:,.0f}')
        stage_analysis['Weighted Value'] = stage_analysis['Weighted Value'].apply(lambda x: f'${x:,.0f}')
        stage_analysis['Stage Probability'] = stage_analysis['Stage Probability'].apply(lambda x: f'{x:.0%}')
        stage_analysis['Avg Days'] = stage_analysis['Avg Days'].apply(lambda x: f'{x:.0f}')
        stage_analysis['Avg Win Prob'] = stage_analysis['Avg Win Prob'].apply(lambda x: f'{x:.1f}%')
        
        st.dataframe(stage_analysis, use_container_width=True)
    else:
        st.info("No data available for pipeline analysis")

def account_intelligence(filtered_df, companies_df):
    """Account intelligence and strategic analysis"""
    
    # Account Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_accounts = filtered_df['company_name'].nunique()
        st.metric("🏢 Total Accounts", f"{total_accounts:,}", "Active prospects")
    
    with col2:
        strategic_accounts = len(filtered_df[filtered_df['opportunity_value'] >= 500000]['company_name'].unique())
        st.metric("💎 Strategic Accounts", strategic_accounts, "$500K+ potential")
    
    with col3:
        multi_opp_accounts = len(filtered_df.groupby('company_name').size()[filtered_df.groupby('company_name').size() > 1])
        st.metric("🎯 Multi-Opportunity", multi_opp_accounts, "Cross-sell potential")
    
    with col4:
        avg_account_value = filtered_df.groupby('company_name')['opportunity_value'].sum().mean()
        st.metric("📈 Avg Account Value", f"${avg_account_value:,.0f}", "Per account pipeline")
    
    # Top Strategic Accounts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Top Strategic Accounts")
        
        account_analysis = filtered_df.groupby('company_name').agg({
            'opportunity_value': 'sum',
            'opportunity_id': 'count',
            'temperature_score': 'mean',
            'win_probability_ai': 'mean',
            'company_industry': 'first',
            'company_size': 'first'
        }).sort_values('opportunity_value', ascending=False).head(15)
        
        for i, (company, data) in enumerate(account_analysis.iterrows()):
            rank_emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
            
            with st.expander(f"{rank_emoji} {company} - ${data['opportunity_value']:,.0f}"):
                col_a, col_b, col_c = st.columns(3)
                
                with col_a:
                    st.metric("Pipeline", f"${data['opportunity_value']:,.0f}")
                    st.metric("Opportunities", data['opportunity_id'])
                
                with col_b:
                    st.markdown(f"**Industry:** {data['company_industry']}")
                    st.markdown(f"**Size:** {data['company_size']}")
                
                with col_c:
                    st.metric("Temperature", f"{data['temperature_score']:.0f}/100")
                    st.metric("Win Prob", f"{data['win_probability_ai']:.0f}%")
    
    with col2:
        st.subheader("🏭 Industry Analysis")
        
        if len(filtered_df) > 0:
            industry_data = filtered_df.groupby('company_industry').agg({
                'opportunity_value': 'sum',
                'company_name': 'nunique',
                'temperature_score': 'mean'
            }).sort_values('opportunity_value', ascending=False)
            
            fig = px.bar(
                industry_data.reset_index().head(10),
                x='opportunity_value',
                y='company_industry',
                title='Top 10 Industries by Pipeline Value',
                orientation='h',
                color='temperature_score',
                color_continuous_scale='RdYlBu_r'
            )
            
            fig.update_layout(
                xaxis_title="Pipeline Value ($)",
                yaxis_title="Industry"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available for industry analysis")

def sales_performance(filtered_df, sales_team_df):
    """Sales performance analytics and scorecards"""
    
    # Performance Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if len(filtered_df) > 0:
            top_performer = filtered_df.groupby('sales_rep_name')['opportunity_value'].sum().idxmax()
            top_value = filtered_df.groupby('sales_rep_name')['opportunity_value'].sum().max()
        else:
            top_performer = "No data"
            top_value = 0
        
        st.metric("🏆 Top Performer", top_performer, f"${top_value:,.0f} pipeline")
    
    with col2:
        if len(filtered_df) > 0:
            avg_quota_attainment = filtered_df.groupby('sales_rep_name').apply(
                lambda x: (x['opportunity_value'].sum() / x['sales_rep_quota'].iloc[0]) * 100
            ).mean()
        else:
            avg_quota_attainment = 0
        
        st.metric("🎯 Avg Quota Attainment", f"{avg_quota_attainment:.1f}%", "Pipeline vs quota")
    
    with col3:
        elite_reps = len(filtered_df[filtered_df['sales_rep_tier'] == 'Elite']['sales_rep_name'].unique()) if len(filtered_df) > 0 else 0
        st.metric("⭐ Elite Sales Reps", elite_reps, "Top tier performers")
    
    with col4:
        avg_temp_by_rep = filtered_df.groupby('sales_rep_name')['temperature_score'].mean().mean() if len(filtered_df) > 0 else 0
        st.metric("🌡️ Team Temperature", f"{avg_temp_by_rep:.1f}", "Average across reps")
    
    # Sales Rep Performance Cards
    st.subheader("👥 Individual Sales Rep Performance")
    
    if len(filtered_df) > 0:
        rep_performance = filtered_df.groupby('sales_rep_name').agg({
            'opportunity_value': 'sum',
            'opportunity_id': 'count',
            'temperature_score': 'mean',
            'win_probability_ai': 'mean',
            'sales_rep_quota': 'first',
            'sales_rep_tier': 'first',
            'sales_rep_region': 'first',
            'sales_rep_specialty': 'first'
        }).sort_values('opportunity_value', ascending=False)
        
        for rep_name, data in rep_performance.iterrows():
            quota_attainment = (data['opportunity_value'] / data['sales_rep_quota']) * 100
            
            # Color coding based on performance
            if data['sales_rep_tier'] == 'Elite' and quota_attainment >= 80:
                color = "success"
            elif quota_attainment >= 60:
                color = "info"
            else:
                color = "warning"
            
            with st.expander(f"{rep_name} - {data['sales_rep_tier']} • {data['sales_rep_region']} • {data['sales_rep_specialty']}"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Pipeline", f"${data['opportunity_value']:,.0f}")
                    st.metric("Quota", f"${data['sales_rep_quota']:,.0f}")
                
                with col2:
                    st.metric("Attainment", f"{quota_attainment:.1f}%", delta=f"{quota_attainment-100:.1f}%")
                    st.metric("Opportunities", data['opportunity_id'])
                
                with col3:
                    st.metric("Avg Temperature", f"{data['temperature_score']:.0f}/100")
                    st.metric("Avg Win Prob", f"{data['win_probability_ai']:.0f}%")
                
                # Progress bar for quota attainment
                st.progress(min(1.0, quota_attainment/100))
    else:
        st.info("No sales performance data available with current filters")

def revenue_forecasting(filtered_df):
    """Advanced revenue forecasting with scenarios"""
    
    # Forecast Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        commit_forecast = filtered_df[filtered_df['forecast_category'] == 'Commit']['weighted_value'].sum()
        st.metric("✅ Commit Forecast", f"${commit_forecast:,.0f}", "High confidence")
    
    with col2:
        best_case = filtered_df[filtered_df['forecast_category'].isin(['Commit', 'Best Case'])]['weighted_value'].sum()
        st.metric("🎯 Best Case", f"${best_case:,.0f}", "Optimistic scenario")
    
    with col3:
        pipeline_forecast = filtered_df['weighted_value'].sum()
        st.metric("📊 Pipeline Forecast", f"${pipeline_forecast:,.0f}", "All opportunities")
    
    with col4:
        confidence_level = (commit_forecast / pipeline_forecast) * 100 if pipeline_forecast > 0 else 0
        st.metric("📈 Confidence Level", f"{confidence_level:.1f}%", "Forecast accuracy")
    
    # Forecast Scenarios
    st.subheader("🎯 Revenue Forecast Scenarios")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        conservative = filtered_df[filtered_df['win_probability_ai'] >= 80]['opportunity_value'].sum() * 0.7
        
        with st.container():
            st.info("### 🔒 Conservative Scenario")
            st.metric("Forecast", f"${conservative:,.0f}")
            st.markdown("""
            **Probability:** 90%  
            **Basis:** High-probability deals with 70% discount factor  
            **Risk:** Very Low
            """)
    
    with col2:
        realistic = filtered_df[filtered_df['win_probability_ai'] >= 60]['weighted_value'].sum()
        
        with st.container():
            st.warning("### 🎯 Realistic Scenario")
            st.metric("Forecast", f"${realistic:,.0f}")
            st.markdown("""
            **Probability:** 70%  
            **Basis:** Weighted pipeline for moderate+ probability deals  
            **Risk:** Medium
            """)
    
    with col3:
        optimistic = filtered_df['weighted_value'].sum() * 1.2
        
        with st.container():
            st.success("### 🚀 Optimistic Scenario")
            st.metric("Forecast", f"${optimistic:,.0f}")
            st.markdown("""
            **Probability:** 40%  
            **Basis:** Full weighted pipeline with 20% upside  
            **Risk:** High
            """)
    
    # Monthly Forecast Chart
    st.subheader("📈 Monthly Revenue Forecast")
    
    # Create monthly forecast data
    if len(filtered_df) > 0:
        monthly_data = []
        current_date = datetime.now()
        
        for i in range(12):
            month_start = current_date + timedelta(days=30*i)
            month_end = month_start + timedelta(days=30)
            
            month_opps = filtered_df[
                (filtered_df['expected_close_date'] >= month_start) & 
                (filtered_df['expected_close_date'] < month_end)
            ]
            
            conservative = month_opps[month_opps['win_probability_ai'] >= 80]['opportunity_value'].sum() * 0.7
            realistic = month_opps[month_opps['win_probability_ai'] >= 60]['weighted_value'].sum()
            optimistic = month_opps['weighted_value'].sum() * 1.2
            
            monthly_data.append({
                'Month': month_start.strftime('%Y-%m'),
                'Conservative': conservative,
                'Realistic': realistic,
                'Optimistic': optimistic
            })
        
        forecast_df = pd.DataFrame(monthly_data)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=forecast_df['Month'],
            y=forecast_df['Conservative'],
            name='Conservative',
            line=dict(color='#e74c3c', width=3),
            mode='lines+markers'
        ))
        
        fig.add_trace(go.Scatter(
            x=forecast_df['Month'],
            y=forecast_df['Realistic'],
            name='Realistic',
            line=dict(color='#f39c12', width=3),
            mode='lines+markers'
        ))
        
        fig.add_trace(go.Scatter(
            x=forecast_df['Month'],
            y=forecast_df['Optimistic'],
            name='Optimistic',
            line=dict(color='#2ecc71', width=3),
            mode='lines+markers'
        ))
        
        fig.update_layout(
            title='12-Month Revenue Forecast by Scenario',
            xaxis_title='Month',
            yaxis_title='Revenue ($)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available for forecast chart")
    
    # Risk Mitigation Recommendations
    st.subheader("⚠️ Risk Assessment & Mitigation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        high_risk_opps = filtered_df[filtered_df['risk_level'] == 'High']
        risk_value = high_risk_opps['opportunity_value'].sum()
        
        with st.container():
            st.error("### 🚨 High-Risk Opportunities")
            st.metric("Count", len(high_risk_opps))
            st.metric("Value at Risk", f"${risk_value:,.0f}")
            st.markdown("""
            **Mitigation Actions:**
            - Schedule executive engagement calls
            - Conduct competitive analysis
            - Implement win-back strategies
            - Escalate to management
            """)
    
    with col2:
        stalled_opps = filtered_df[filtered_df['days_in_stage'] > 60]
        stalled_value = stalled_opps['opportunity_value'].sum()
        
        with st.container():
            st.warning("### ⏰ Stalled Opportunities")
            st.metric("Count", len(stalled_opps))
            st.metric("Stalled Value", f"${stalled_value:,.0f}")
            st.markdown("""
            **Recovery Actions:**
            - Re-engage decision makers
            - Reassess customer needs
            - Adjust value proposition
            - Set new timeline milestones
            """)

# Run the application
if __name__ == "__main__":
    main()

    
