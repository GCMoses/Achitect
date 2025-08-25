import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker
import json

# Page configuration
st.set_page_config(
    page_title="Producer Performance Hub",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for ultra-modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    
    .producer-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    }
    
    .top-performer {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border: 2px solid #667eea;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stTab > div > div > div > div {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 10px;
        padding: 0.5rem 1rem;
        margin: 0.2rem;
        color: white;
        font-weight: bold;
    }
    
    .dark-mode {
        background: linear-gradient(135deg, #232526 0%, #414345 100%);
        color: white;
    }
    
    .light-mode {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Faker for realistic data
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

@st.cache_data
def generate_comprehensive_data():
    """Generate comprehensive mock data for insurance producers"""
    
    # Producer data with realistic profiles
    producers = [
        {"id": 1, "name": "Sarah Chen", "email": "sarah.chen@nexusinsure.com", "phone": "(555) 123-4567", 
         "region": "West Coast", "hire_date": "2020-03-15", "tier": "Elite", "specialty": "Commercial Property"},
        {"id": 2, "name": "Marcus Rodriguez", "email": "marcus.r@nexusinsure.com", "phone": "(555) 234-5678", 
         "region": "Southwest", "hire_date": "2019-07-22", "tier": "Elite", "specialty": "Cyber Security"},
        {"id": 3, "name": "Elena Volkov", "email": "elena.v@nexusinsure.com", "phone": "(555) 345-6789", 
         "region": "Northeast", "hire_date": "2018-01-10", "tier": "Elite", "specialty": "Professional Liability"},
        {"id": 4, "name": "James Kim", "email": "james.kim@nexusinsure.com", "phone": "(555) 456-7890", 
         "region": "Southeast", "hire_date": "2021-05-03", "tier": "Platinum", "specialty": "General Liability"},
        {"id": 5, "name": "Isabella Foster", "email": "isabella.f@nexusinsure.com", "phone": "(555) 567-8901", 
         "region": "Midwest", "hire_date": "2020-09-18", "tier": "Elite", "specialty": "Directors & Officers"},
        {"id": 6, "name": "David Park", "email": "david.park@nexusinsure.com", "phone": "(555) 678-9012", 
         "region": "West Coast", "hire_date": "2022-02-14", "tier": "Gold", "specialty": "Workers Compensation"},
        {"id": 7, "name": "Zoe Williams", "email": "zoe.w@nexusinsure.com", "phone": "(555) 789-0123", 
         "region": "Northeast", "hire_date": "2017-11-30", "tier": "Elite", "specialty": "Commercial Property"},
        {"id": 8, "name": "Ahmed Hassan", "email": "ahmed.h@nexusinsure.com", "phone": "(555) 890-1234", 
         "region": "Southeast", "hire_date": "2019-04-12", "tier": "Elite", "specialty": "Cyber Security"},
        {"id": 9, "name": "Sophie Turner", "email": "sophie.t@nexusinsure.com", "phone": "(555) 901-2345", 
         "region": "Midwest", "hire_date": "2021-08-07", "tier": "Platinum", "specialty": "Professional Liability"},
        {"id": 10, "name": "Ryan O'Connor", "email": "ryan.o@nexusinsure.com", "phone": "(555) 012-3456", 
         "region": "West Coast", "hire_date": "2020-12-01", "tier": "Gold", "specialty": "General Liability"}
    ]
    
    # Modern company names and details
    companies = [
        {"name": "TechNova Solutions", "industry": "Technology", "size": "Enterprise", "revenue": 50000000},
        {"name": "Quantum Dynamics Corp", "industry": "Manufacturing", "size": "Fortune 500", "revenue": 200000000},
        {"name": "Stellar Manufacturing", "industry": "Manufacturing", "size": "Mid-Market", "revenue": 25000000},
        {"name": "EcoFlow Industries", "industry": "Energy", "size": "Enterprise", "revenue": 75000000},
        {"name": "CyberShield Security", "industry": "Technology", "size": "Mid-Market", "revenue": 30000000},
        {"name": "NextGen Robotics", "industry": "Technology", "size": "Startup", "revenue": 5000000},
        {"name": "BioTech Innovations", "industry": "Healthcare", "size": "Enterprise", "revenue": 100000000},
        {"name": "CloudFirst Systems", "industry": "Technology", "size": "Mid-Market", "revenue": 20000000},
        {"name": "DataStream Analytics", "industry": "Technology", "size": "Small Business", "revenue": 8000000},
        {"name": "GreenTech Ventures", "industry": "Energy", "size": "Mid-Market", "revenue": 35000000},
        {"name": "Digital Frontier Inc", "industry": "Technology", "size": "Enterprise", "revenue": 60000000},
        {"name": "SmartGrid Technologies", "industry": "Energy", "size": "Enterprise", "revenue": 80000000},
        {"name": "FusionPoint Energy", "industry": "Energy", "size": "Fortune 500", "revenue": 300000000},
        {"name": "NanoTech Materials", "industry": "Manufacturing", "size": "Mid-Market", "revenue": 40000000},
        {"name": "AeroSpace Dynamics", "industry": "Aerospace", "size": "Enterprise", "revenue": 120000000},
        {"name": "PharmaCore Research", "industry": "Healthcare", "size": "Enterprise", "revenue": 90000000},
        {"name": "AgriTech Solutions", "industry": "Agriculture", "size": "Mid-Market", "revenue": 22000000},
        {"name": "MetaVerse Industries", "industry": "Technology", "size": "Startup", "revenue": 12000000},
        {"name": "BlockChain Systems", "industry": "Technology", "size": "Mid-Market", "revenue": 28000000},
        {"name": "AI-Powered Logistics", "industry": "Logistics", "size": "Enterprise", "revenue": 65000000}
    ]
    
    # Insurance carriers
    carriers = [
        "AIG", "Zurich", "Liberty Mutual", "Travelers", "Hartford", "Chubb", "Allianz", "Marsh", 
        "Willis Towers Watson", "Aon", "Berkshire Hathaway", "CNA", "Nationwide", "Progressive Commercial",
        "State Farm Commercial", "Allstate Commercial", "USAA", "Farmers Commercial", "MetLife", "Prudential"
    ]
    
    # Policy types and details
    policy_types = [
        {"type": "Commercial Property", "avg_premium": 45000, "commission_rate": 0.12},
        {"type": "General Liability", "avg_premium": 25000, "commission_rate": 0.10},
        {"type": "Cyber Security", "avg_premium": 35000, "commission_rate": 0.15},
        {"type": "Workers Compensation", "avg_premium": 30000, "commission_rate": 0.08},
        {"type": "Professional Liability", "avg_premium": 40000, "commission_rate": 0.14},
        {"type": "Directors & Officers", "avg_premium": 60000, "commission_rate": 0.16},
        {"type": "Employment Practices", "avg_premium": 28000, "commission_rate": 0.11},
        {"type": "Commercial Auto", "avg_premium": 20000, "commission_rate": 0.09},
        {"type": "Umbrella Policy", "avg_premium": 15000, "commission_rate": 0.13},
        {"type": "Product Liability", "avg_premium": 50000, "commission_rate": 0.17}
    ]
    
    # Referral sources
    referral_sources = [
        "LinkedIn", "Industry Conference", "Client Referral", "Broker Network", "Cold Outreach", 
        "Trade Association", "Chamber of Commerce", "Online Lead", "Partner Referral", "Renewal"
    ]
    
    # Generate comprehensive policy data
    policies = []
    for i in range(2000):  # Generate 2000 policies for rich data
        producer = random.choice(producers)
        company = random.choice(companies)
        policy_type = random.choice(policy_types)
        carrier = random.choice(carriers)
        referral = random.choice(referral_sources)
        
        # Create realistic premium variations
        base_premium = policy_type["avg_premium"]
        premium_variation = random.uniform(0.7, 1.8)  # 70% to 180% of base
        premium = int(base_premium * premium_variation)
        
        # Calculate commission
        commission = int(premium * policy_type["commission_rate"])
        
        # Generate dates
        created_date = fake.date_time_between(start_date='-2y', end_date='now')
        effective_date = created_date + timedelta(days=random.randint(1, 60))
        expiration_date = effective_date + timedelta(days=365)
        
        # Status logic
        if created_date < datetime.now() - timedelta(days=30):
            status = random.choices(
                ["Active", "Expired", "Cancelled", "Renewed"], 
                weights=[60, 15, 10, 15]
            )[0]
        else:
            status = random.choices(
                ["Active", "Pending", "Quoted"], 
                weights=[40, 35, 25]
            )[0]
        
        policy = {
            "policy_id": f"POL-{i+1:06d}",
            "producer_id": producer["id"],
            "producer_name": producer["name"],
            "producer_region": producer["region"],
            "producer_tier": producer["tier"],
            "producer_specialty": producer["specialty"],
            "company_name": company["name"],
            "company_industry": company["industry"],
            "company_size": company["size"],
            "company_revenue": company["revenue"],
            "policy_type": policy_type["type"],
            "carrier": carrier,
            "referral_source": referral,
            "premium": premium,
            "commission": commission,
            "commission_rate": policy_type["commission_rate"],
            "status": status,
            "created_date": created_date,
            "effective_date": effective_date,
            "expiration_date": expiration_date,
            "probability": random.randint(60, 95) if status == "Pending" else 100,
            "days_to_close": random.randint(15, 120) if status == "Pending" else 0,
            "customer_satisfaction": random.randint(3, 5),
            "risk_score": random.randint(1, 100),
            "renewal_probability": random.randint(70, 95) if status == "Active" else 0,
            "bind_ratio": random.uniform(0.65, 0.95),
            "quote_to_bind_days": random.randint(5, 45),
            "claims_history": random.randint(0, 3),
            "policy_limit": random.choice([1000000, 2000000, 5000000, 10000000]),
            "deductible": random.choice([1000, 2500, 5000, 10000, 25000])
        }
        
        policies.append(policy)
    
    return pd.DataFrame(policies), pd.DataFrame(producers), pd.DataFrame(companies)

# Load data
@st.cache_data
def load_data():
    policies_df, producers_df, companies_df = generate_comprehensive_data()
    
    # Ensure datetime columns are properly formatted
    policies_df['created_date'] = pd.to_datetime(policies_df['created_date'])
    policies_df['effective_date'] = pd.to_datetime(policies_df['effective_date'])
    policies_df['expiration_date'] = pd.to_datetime(policies_df['expiration_date'])
    
    return policies_df, producers_df, companies_df

# Theme toggle
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Main app
def main():
    # Load data
    policies_df, producers_df, companies_df = load_data()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; margin: 0; font-size: 2.5rem; font-weight: bold;">
            🎯 Producer Performance Hub
        </h1>
        <p style="color: rgba(255,255,255,0.8); margin: 0.5rem 0 0 0; font-size: 1.1rem;">
            Enterprise-Grade Insurance Analytics & Producer Scorecards
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Theme toggle
    col1, col2 = st.columns([6, 1])
    with col2:
        if st.button("🌓 Toggle Theme"):
            toggle_theme()
    
    # Sidebar filters
    st.sidebar.markdown("### 🎛️ Smart Filters")
    
    # Producer filter
    producer_options = ["All Producers"] + list(producers_df['name'].unique())
    selected_producer = st.sidebar.selectbox("Select Producer", producer_options)
    
    # Other filters
    policy_types = ["All Types"] + list(policies_df['policy_type'].unique())
    selected_policy_type = st.sidebar.selectbox("Policy Type", policy_types)
    
    statuses = ["All Statuses"] + list(policies_df['status'].unique())
    selected_status = st.sidebar.selectbox("Status", statuses)
    
    regions = ["All Regions"] + list(policies_df['producer_region'].unique())
    selected_region = st.sidebar.selectbox("Region", regions)
    
    carriers = ["All Carriers"] + list(policies_df['carrier'].unique())
    selected_carrier = st.sidebar.selectbox("Carrier", carriers)
    
    # Date range filter
    min_date = policies_df['created_date'].min().date()
    max_date = policies_df['created_date'].max().date()
    
    date_range = st.sidebar.date_input(
        "Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Apply filters
    filtered_df = policies_df.copy()
    
    if selected_producer != "All Producers":
        filtered_df = filtered_df[filtered_df['producer_name'] == selected_producer]
    
    if selected_policy_type != "All Types":
        filtered_df = filtered_df[filtered_df['policy_type'] == selected_policy_type]
        
    if selected_status != "All Statuses":
        filtered_df = filtered_df[filtered_df['status'] == selected_status]
        
    if selected_region != "All Regions":
        filtered_df = filtered_df[filtered_df['producer_region'] == selected_region]
        
    if selected_carrier != "All Carriers":
        filtered_df = filtered_df[filtered_df['carrier'] == selected_carrier]
    
    if len(date_range) == 2:
        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[1]) + pd.Timedelta(days=1)  # Include end date
        filtered_df = filtered_df[
            (filtered_df['created_date'] >= start_date) & 
            (filtered_df['created_date'] < end_date)
        ]
    
    # Main tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Executive Dashboard", 
        "🏆 Producer Scorecards", 
        "📈 Performance Analytics", 
        "💼 Policy Intelligence",
        "🎯 Top Performers"
    ])
    
    with tab1:
        executive_dashboard(filtered_df, policies_df)
    
    with tab2:
        producer_scorecards(filtered_df, producers_df, selected_producer)
    
    with tab3:
        performance_analytics(filtered_df)
    
    with tab4:
        policy_intelligence(filtered_df)
    
    with tab5:
        top_performers(filtered_df)

def executive_dashboard(filtered_df, full_df):
    """Executive Dashboard with KPIs and overview charts"""
    
    # KPIs
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_premium = filtered_df['premium'].sum()
        st.markdown(f"""
        <div class="metric-card">
            <h3>💰 Total Premium</h3>
            <h2>${total_premium:,.0f}</h2>
            <p>+12.5% vs last period</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        total_policies = len(filtered_df)
        st.markdown(f"""
        <div class="metric-card">
            <h3>📄 Total Policies</h3>
            <h2>{total_policies:,}</h2>
            <p>+8.3% vs last period</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        avg_premium = filtered_df['premium'].mean()
        st.markdown(f"""
        <div class="metric-card">
            <h3>📊 Avg Premium</h3>
            <h2>${avg_premium:,.0f}</h2>
            <p>+5.7% vs last period</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        bind_rate = (filtered_df['status'] == 'Active').mean() * 100
        st.markdown(f"""
        <div class="metric-card">
            <h3>🎯 Bind Rate</h3>
            <h2>{bind_rate:.1f}%</h2>
            <p>+2.1% vs last period</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        total_commission = filtered_df['commission'].sum()
        st.markdown(f"""
        <div class="metric-card">
            <h3>💵 Total Commission</h3>
            <h2>${total_commission:,.0f}</h2>
            <p>+15.2% vs last period</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Premium by Policy Type")
        policy_premium = filtered_df.groupby('policy_type')['premium'].sum().sort_values(ascending=False)
        fig = px.bar(
            x=policy_premium.index,
            y=policy_premium.values,
            title="Premium Distribution by Policy Type",
            labels={'x': 'Policy Type', 'y': 'Premium ($)'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌍 Premium by Region")
        region_premium = filtered_df.groupby('producer_region')['premium'].sum()
        fig = px.pie(
            values=region_premium.values,
            names=region_premium.index,
            title="Premium Distribution by Region"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Time series
    st.subheader("📊 Monthly Premium Trends")
    monthly_data = filtered_df.groupby(filtered_df['created_date'].dt.to_period('M')).agg({
        'premium': 'sum',
        'commission': 'sum',
        'policy_id': 'count'
    }).reset_index()
    monthly_data['created_date'] = monthly_data['created_date'].astype(str)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    fig.add_trace(
        go.Scatter(
            x=monthly_data['created_date'],
            y=monthly_data['premium'],
            name="Premium",
            line=dict(color='#667eea', width=3)
        ),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(
            x=monthly_data['created_date'],
            y=monthly_data['policy_id'],
            name="Policy Count",
            line=dict(color='#f093fb', width=3)
        ),
        secondary_y=True,
    )
    
    fig.update_layout(
        title="Monthly Premium and Policy Count Trends",
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12),
        title_font=dict(size=16, color='#667eea')
    )
    
    fig.update_yaxes(title_text="Premium ($)", secondary_y=False)
    fig.update_yaxes(title_text="Policy Count", secondary_y=True)
    
    st.plotly_chart(fig, use_container_width=True)

def producer_scorecards(filtered_df, producers_df, selected_producer):
    """Detailed producer scorecards with comprehensive metrics"""
    
    if selected_producer == "All Producers":
        st.subheader("🏆 Producer Performance Overview")
        
        # Producer summary stats
        producer_stats = filtered_df.groupby('producer_name').agg({
            'premium': ['sum', 'mean', 'count'],
            'commission': 'sum',
            'policy_id': 'count',
            'customer_satisfaction': 'mean',
            'bind_ratio': 'mean'
        }).round(2)
        
        producer_stats.columns = ['Total Premium', 'Avg Premium', 'Premium Count', 'Total Commission', 
                                'Policy Count', 'Avg Satisfaction', 'Bind Rate']
        
        # Add rankings
        producer_stats['Premium Rank'] = producer_stats['Total Premium'].rank(method='dense', ascending=False)
        producer_stats['Commission Rank'] = producer_stats['Total Commission'].rank(method='dense', ascending=False)
        
        # Display top performers
        st.markdown("### 🥇 Top 5 Producers by Premium")
        top_5 = producer_stats.nlargest(5, 'Total Premium')
        
        for i, (producer, stats) in enumerate(top_5.iterrows()):
            rank_emoji = ["🥇", "🥈", "🥉", "🏅", "🏅"][i]
            st.markdown(f"""
            <div class="{'top-performer' if i < 3 else 'producer-card'}">
                <h4>{rank_emoji} {producer}</h4>
                <div style="display: flex; justify-content: space-between;">
                    <div>
                        <p><strong>Premium:</strong> ${stats['Total Premium']:,.0f}</p>
                        <p><strong>Policies:</strong> {stats['Policy Count']:.0f}</p>
                        <p><strong>Satisfaction:</strong> {stats['Avg Satisfaction']:.1f}/5</p>
                    </div>
                    <div>
                        <p><strong>Commission:</strong> ${stats['Total Commission']:,.0f}</p>
                        <p><strong>Bind Rate:</strong> {stats['Bind Rate']:.1%}</p>
                        <p><strong>Avg Premium:</strong> ${stats['Avg Premium']:,.0f}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Producer comparison chart
        st.subheader("📊 Producer Performance Comparison")
        
        fig = px.scatter(
            producer_stats.reset_index(),
            x='Policy Count',
            y='Total Premium',
            size='Total Commission',
            color='Avg Satisfaction',
            hover_name='producer_name',
            title="Producer Performance Matrix",
            labels={'Policy Count': 'Number of Policies', 'Total Premium': 'Total Premium ($)'}
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        # Individual producer scorecard
        st.subheader(f"🎯 {selected_producer} - Complete Scorecard")
        
        producer_data = filtered_df[filtered_df['producer_name'] == selected_producer]
        
        if len(producer_data) == 0:
            st.warning("No data available for the selected producer.")
            return
        
        # Producer info
        producer_info = producers_df[producers_df['name'] == selected_producer].iloc[0]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="producer-card">
                <h4>👤 Producer Details</h4>
                <p><strong>Name:</strong> {producer_info['name']}</p>
                <p><strong>Region:</strong> {producer_info['region']}</p>
                <p><strong>Tier:</strong> {producer_info['tier']}</p>
                <p><strong>Specialty:</strong> {producer_info['specialty']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            total_premium = producer_data['premium'].sum()
            total_policies = len(producer_data)
            avg_premium = producer_data['premium'].mean()
            
            st.markdown(f"""
            <div class="producer-card">
                <h4>💰 Performance Metrics</h4>
                <p><strong>Total Premium:</strong> ${total_premium:,.0f}</p>
                <p><strong>Total Policies:</strong> {total_policies}</p>
                <p><strong>Avg Premium:</strong> ${avg_premium:,.0f}</p>
                <p><strong>Total Commission:</strong> ${producer_data['commission'].sum():,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            bind_rate = (producer_data['status'] == 'Active').mean()
            avg_satisfaction = producer_data['customer_satisfaction'].mean()
            
            st.markdown(f"""
            <div class="producer-card">
                <h4>🎯 Quality Metrics</h4>
                <p><strong>Bind Rate:</strong> {bind_rate:.1%}</p>
                <p><strong>Avg Satisfaction:</strong> {avg_satisfaction:.1f}/5</p>
                <p><strong>Avg Risk Score:</strong> {producer_data['risk_score'].mean():.0f}</p>
                <p><strong>Renewal Rate:</strong> {producer_data['renewal_probability'].mean():.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Producer's policy distribution
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Policy Type Distribution")
            policy_dist = producer_data.groupby('policy_type')['premium'].sum().sort_values(ascending=False)
            
            fig = px.bar(
                x=policy_dist.index,
                y=policy_dist.values,
                title=f"{selected_producer}'s Premium by Policy Type"
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12),
                title_font=dict(size=16, color='#667eea')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📈 Monthly Performance Trend")
            monthly_producer = producer_data.groupby(producer_data['created_date'].dt.to_period('M')).agg({
                'premium': 'sum',
                'policy_id': 'count'
            }).reset_index()
            monthly_producer['created_date'] = monthly_producer['created_date'].astype(str)
            
            fig = px.line(
                monthly_producer,
                x='created_date',
                y='premium',
                title=f"{selected_producer}'s Monthly Premium Trend",
                markers=True
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12),
                title_font=dict(size=16, color='#667eea')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Producer ranking and expertise analysis
        st.subheader("🏆 Producer Rankings & Expertise")
        
        # Calculate rankings across all producers
        all_producer_stats = filtered_df.groupby('producer_name').agg({
            'premium': 'sum',
            'commission': 'sum',
            'policy_id': 'count',
            'customer_satisfaction': 'mean',
            'bind_ratio': 'mean'
        })
        
        producer_rank_premium = all_producer_stats['premium'].rank(method='dense', ascending=False)
        producer_rank_policies = all_producer_stats['policy_id'].rank(method='dense', ascending=False)
        producer_rank_satisfaction = all_producer_stats['customer_satisfaction'].rank(method='dense', ascending=False)
        
        current_producer_premium_rank = producer_rank_premium[selected_producer]
        current_producer_policies_rank = producer_rank_policies[selected_producer]
        current_producer_satisfaction_rank = producer_rank_satisfaction[selected_producer]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            rank_color = "🥇" if current_producer_premium_rank <= 3 else "🥈" if current_producer_premium_rank <= 5 else "🥉"
            st.markdown(f"""
            <div class="metric-card">
                <h4>{rank_color} Premium Ranking</h4>
                <h2>#{int(current_producer_premium_rank)}</h2>
                <p>out of {len(all_producer_stats)} producers</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            rank_color = "🥇" if current_producer_policies_rank <= 3 else "🥈" if current_producer_policies_rank <= 5 else "🥉"
            st.markdown(f"""
            <div class="metric-card">
                <h4>{rank_color} Policy Volume Ranking</h4>
                <h2>#{int(current_producer_policies_rank)}</h2>
                <p>out of {len(all_producer_stats)} producers</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            rank_color = "🥇" if current_producer_satisfaction_rank <= 3 else "🥈" if current_producer_satisfaction_rank <= 5 else "🥉"
            st.markdown(f"""
            <div class="metric-card">
                <h4>{rank_color} Satisfaction Ranking</h4>
                <h2>#{int(current_producer_satisfaction_rank)}</h2>
                <p>out of {len(all_producer_stats)} producers</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Producer's expertise analysis
        st.subheader("🎯 Expertise Analysis")
        
        # Policy type expertise
        producer_policy_expertise = producer_data.groupby('policy_type').agg({
            'premium': ['sum', 'count', 'mean'],
            'bind_ratio': 'mean',
            'customer_satisfaction': 'mean'
        }).round(2)
        
        producer_policy_expertise.columns = ['Total Premium', 'Policy Count', 'Avg Premium', 'Bind Rate', 'Satisfaction']
        producer_policy_expertise = producer_policy_expertise.sort_values('Total Premium', ascending=False)
        
        st.dataframe(
            producer_policy_expertise,
            use_container_width=True
        )
        
        # Carrier relationships
        st.subheader("🤝 Carrier Relationships")
        carrier_performance = producer_data.groupby('carrier').agg({
            'premium': 'sum',
            'policy_id': 'count',
            'bind_ratio': 'mean'
        }).sort_values('premium', ascending=False).head(10)
        
        fig = px.bar(
            carrier_performance.reset_index(),
            x='carrier',
            y='premium',
            title=f"{selected_producer}'s Top Carriers by Premium",
            labels={'carrier': 'Carrier', 'premium': 'Premium ($)'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)

def performance_analytics(filtered_df):
    """Advanced performance analytics and insights"""
    
    st.subheader("📈 Advanced Performance Analytics")
    
    # Performance metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_days_to_close = filtered_df[filtered_df['status'] == 'Active']['quote_to_bind_days'].mean()
        st.metric(
            label="Avg Days to Bind",
            value=f"{avg_days_to_close:.0f} days",
            delta="-3.2 days"
        )
    
    with col2:
        conversion_rate = (filtered_df['status'] == 'Active').mean() * 100
        st.metric(
            label="Quote to Bind Rate",
            value=f"{conversion_rate:.1f}%",
            delta="2.3%"
        )
    
    with col3:
        avg_policy_limit = filtered_df['policy_limit'].mean()
        st.metric(
            label="Avg Policy Limit",
            value=f"${avg_policy_limit/1000000:.1f}M",
            delta="$0.2M"
        )
    
    with col4:
        retention_rate = filtered_df['renewal_probability'].mean()
        st.metric(
            label="Retention Rate",
            value=f"{retention_rate:.1f}%",
            delta="1.8%"
        )
    
    # Advanced charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💼 Premium vs Policy Limit Analysis")
        fig = px.scatter(
            filtered_df,
            x='policy_limit',
            y='premium',
            color='policy_type',
            size='commission',
            hover_data=['producer_name', 'carrier'],
            title="Premium vs Policy Limit by Type"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("⏱️ Quote to Bind Performance")
        bind_performance = filtered_df[filtered_df['status'] == 'Active'].groupby('producer_name')['quote_to_bind_days'].mean().sort_values()
        
        fig = px.bar(
            x=bind_performance.values[:10],
            y=bind_performance.index[:10],
            orientation='h',
            title="Top 10 Fastest Producers (Days to Bind)",
            labels={'x': 'Average Days to Bind', 'y': 'Producer'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Risk analysis
    st.subheader("⚠️ Risk Analysis Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Risk Score Distribution")
        fig = px.histogram(
            filtered_df,
            x='risk_score',
            nbins=20,
            title="Risk Score Distribution",
            labels={'risk_score': 'Risk Score', 'count': 'Number of Policies'}
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Premium vs Risk Score")
        fig = px.scatter(
            filtered_df,
            x='risk_score',
            y='premium',
            color='policy_type',
            title="Premium vs Risk Score Analysis"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)

def policy_intelligence(filtered_df):
    """Policy intelligence and insights"""
    
    st.subheader("💼 Policy Intelligence Dashboard")
    
    # Top insights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        top_policy = filtered_df.loc[filtered_df['premium'].idxmax()]
        st.markdown(f"""
        <div class="top-performer">
            <h4>🏆 Highest Premium Policy</h4>
            <p><strong>Amount:</strong> ${top_policy['premium']:,.0f}</p>
            <p><strong>Type:</strong> {top_policy['policy_type']}</p>
            <p><strong>Producer:</strong> {top_policy['producer_name']}</p>
            <p><strong>Company:</strong> {top_policy['company_name']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        top_carrier = filtered_df.groupby('carrier')['premium'].sum().idxmax()
        top_carrier_premium = filtered_df.groupby('carrier')['premium'].sum().max()
        st.markdown(f"""
        <div class="top-performer">
            <h4>🥇 Top Carrier</h4>
            <p><strong>Carrier:</strong> {top_carrier}</p>
            <p><strong>Total Premium:</strong> ${top_carrier_premium:,.0f}</p>
            <p><strong>Policies:</strong> {len(filtered_df[filtered_df['carrier'] == top_carrier])}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        top_account = filtered_df.groupby('company_name')['premium'].sum().idxmax()
        top_account_premium = filtered_df.groupby('company_name')['premium'].sum().max()
        st.markdown(f"""
        <div class="top-performer">
            <h4>💎 Top Account</h4>
            <p><strong>Company:</strong> {top_account}</p>
            <p><strong>Total Premium:</strong> ${top_account_premium:,.0f}</p>
            <p><strong>Policies:</strong> {len(filtered_df[filtered_df['company_name'] == top_account])}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Policy type analysis
    st.subheader("📊 Policy Type Performance Analysis")
    
    policy_analysis = filtered_df.groupby('policy_type').agg({
        'premium': ['sum', 'mean', 'count'],
        'commission': 'sum',
        'bind_ratio': 'mean',
        'customer_satisfaction': 'mean',
        'risk_score': 'mean'
    }).round(2)
    
    policy_analysis.columns = [
        'Total Premium', 'Avg Premium', 'Policy Count', 
        'Total Commission', 'Bind Rate', 'Satisfaction', 'Risk Score'
    ]
    
    st.dataframe(policy_analysis, use_container_width=True)
    
    # Carrier performance
    st.subheader("🤝 Carrier Performance Dashboard")
    
    carrier_metrics = filtered_df.groupby('carrier').agg({
        'premium': ['sum', 'count'],
        'commission': 'sum',
        'bind_ratio': 'mean',
        'customer_satisfaction': 'mean'
    }).round(2)
    
    carrier_metrics.columns = ['Total Premium', 'Policy Count', 'Commission', 'Bind Rate', 'Satisfaction']
    carrier_metrics = carrier_metrics.sort_values('Total Premium', ascending=False).head(15)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(
            carrier_metrics.reset_index(),
            x='carrier',
            y='Total Premium',
            title="Top 15 Carriers by Premium Volume"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea'),
            xaxis_tickangle=-45
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.scatter(
            carrier_metrics.reset_index(),
            x='Policy Count',
            y='Total Premium',
            size='Commission',
            color='Satisfaction',
            hover_name='carrier',
            title="Carrier Performance Matrix"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Referral source analysis
    st.subheader("🎯 Referral Source Performance")
    
    referral_performance = filtered_df.groupby('referral_source').agg({
        'premium': 'sum',
        'policy_id': 'count',
        'bind_ratio': 'mean'
    }).sort_values('premium', ascending=False)
    
    top_referrer = referral_performance.index[0]
    top_referrer_premium = referral_performance.iloc[0]['premium']
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.pie(
            values=referral_performance['premium'],
            names=referral_performance.index,
            title="Premium Distribution by Referral Source"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"""
        <div class="top-performer">
            <h4>🎯 Top Referral Source</h4>
            <p><strong>Source:</strong> {top_referrer}</p>
            <p><strong>Premium:</strong> ${top_referrer_premium:,.0f}</p>
            <p><strong>Policies:</strong> {referral_performance.iloc[0]['policy_id']:.0f}</p>
            <p><strong>Bind Rate:</strong> {referral_performance.iloc[0]['bind_ratio']:.1%}</p>
        </div>
        """, unsafe_allow_html=True)

def top_performers(filtered_df):
    """Top performers across all categories"""
    
    st.subheader("🏆 Top Performers Hall of Fame")
    
    # Top performers by different metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🥇 Top 10 Producers by Premium")
        top_producers_premium = filtered_df.groupby('producer_name')['premium'].sum().sort_values(ascending=False).head(10)
        
        for i, (producer, premium) in enumerate(top_producers_premium.items()):
            rank_emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
            policies_count = len(filtered_df[filtered_df['producer_name'] == producer])
            
            st.markdown(f"""
            <div class="producer-card">
                <h5>{rank_emoji} {producer}</h5>
                <p><strong>Premium:</strong> ${premium:,.0f}</p>
                <p><strong>Policies:</strong> {policies_count}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📊 Top 10 Producers by Policy Count")
        top_producers_volume = filtered_df.groupby('producer_name').size().sort_values(ascending=False).head(10)
        
        for i, (producer, count) in enumerate(top_producers_volume.items()):
            rank_emoji = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else f"{i+1}."
            premium_total = filtered_df[filtered_df['producer_name'] == producer]['premium'].sum()
            
            st.markdown(f"""
            <div class="producer-card">
                <h5>{rank_emoji} {producer}</h5>
                <p><strong>Policies:</strong> {count}</p>
                <p><strong>Premium:</strong> ${premium_total:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Performance comparison radar chart
    st.subheader("📈 Top 5 Producers Performance Radar")
    
    top_5_producers = filtered_df.groupby('producer_name')['premium'].sum().sort_values(ascending=False).head(5).index
    
    radar_data = []
    for producer in top_5_producers:
        producer_data = filtered_df[filtered_df['producer_name'] == producer]
        
        metrics = {
            'Premium': (producer_data['premium'].sum() / filtered_df['premium'].sum()) * 100,
            'Policy Count': (len(producer_data) / len(filtered_df)) * 100,
            'Bind Rate': producer_data['bind_ratio'].mean() * 100,
            'Satisfaction': producer_data['customer_satisfaction'].mean() * 20,  # Scale to 100
            'Avg Premium': (producer_data['premium'].mean() / filtered_df['premium'].mean()) * 100
        }
        
        radar_data.append({
            'Producer': producer,
            'Premium': metrics['Premium'],
            'Policy Count': metrics['Policy Count'],
            'Bind Rate': metrics['Bind Rate'],
            'Satisfaction': metrics['Satisfaction'],
            'Avg Premium': metrics['Avg Premium']
        })
    
    # Create radar chart
    categories = ['Premium', 'Policy Count', 'Bind Rate', 'Satisfaction', 'Avg Premium']
    
    fig = go.Figure()
    
    colors = ['#667eea', '#f093fb', '#f5576c', '#4ecdc4', '#45b7d1']
    
    for i, producer_data in enumerate(radar_data):
        values = [producer_data[cat] for cat in categories]
        values += values[:1]  # Complete the circle
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=producer_data['Producer'],
            line_color=colors[i]
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title="Top 5 Producers Performance Comparison",
        font=dict(size=12),
        title_font=dict(size=16, color='#667eea')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Company performance
    st.subheader("🏢 Top Client Companies")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 By Premium Volume")
        top_companies_premium = filtered_df.groupby('company_name')['premium'].sum().sort_values(ascending=False).head(10)
        
        fig = px.bar(
            x=top_companies_premium.values,
            y=top_companies_premium.index,
            orientation='h',
            title="Top 10 Companies by Premium"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📄 By Policy Count")
        top_companies_volume = filtered_df.groupby('company_name').size().sort_values(ascending=False).head(10)
        
        fig = px.bar(
            x=top_companies_volume.values,
            y=top_companies_volume.index,
            orientation='h',
            title="Top 10 Companies by Policy Count"
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(size=12),
            title_font=dict(size=16, color='#667eea')
        )
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
