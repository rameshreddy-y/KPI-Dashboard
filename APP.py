import streamlit as st
import pandas as pd
import datetime
import os
import plotly.graph_objects as go
import base64

# =======================================================================================
# HIGH-STAKE ENTERPRISE EXECUTIVE LIGHT THEME & PROFESSIONAL FOOTER INJECTION (CSS)
# =======================================================================================
st.set_page_config(page_title="V57 Inspection Line Shift Leaders KPI Dashboard", layout="wide")

st.markdown("""
    <style>
    /* Premium Scandinavian Clean Canvas Background */
    .stApp {
        background-color: #ffffff;
        color: #1e293b;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    /* Elegant Corporate Sidebar Structure */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
    
    /* Clean Luxury Metrics Card */
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 22px 18px;
        border-radius: 8px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.03);
    }
    div[data-testid="metric-container"]:hover {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
        border-color: #cbd5e1;
    }
    
    /* Executive Headings Color Configuration */
    h1 {
        color: #0f172a !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em;
        font-size: 2.25rem !important;
    }
    h2, h3 {
        color: #0f172a !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em;
    }
    
    /* High-Stake Customer Labels alignment */
    .stMetric label {
        color: #64748b !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 0.75rem !important;
        letter-spacing: 0.05em;
    }
    
    .stMetric div[data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-weight: 700 !important;
        font-size: 1.75rem !important;
    }
    
    /* Dataframe Table Border Refining */
    .stDataFrame {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        background-color: #ffffff;
        margin-bottom: 50px; /* Space for footer */
    }
    
    /* Custom divider line styling */
    hr {
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        border: 0;
        border-top: 1px solid #f1f5f9;
    }

    /* Professional Formal Fixed Footer Styling */
    .corporate-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8fafc;
        color: #64748b;
        text-align: center;
        padding: 8px 0;
        font-size: 0.78rem;
        font-weight: 500;
        letter-spacing: 0.025em;
        border-top: 1px solid #e2e8f0;
        z-index: 999;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

database_filename = "kpi_database.csv"

# PERFECT STANDARD SCHEMA (1 TO 12 IN EXACT CHRONOLOGICAL ORDER)
headers = [
    "Date", "Engineer Name", "Shift", 
    "1. Safety Incidents (Qty)", 
    "2. 5S Audit Score (%)", 
    "3. Near Miss / Suggestions (Qty)", 
    "4. Kaizen Raised vs Closed (Qty)",
    "5. Zero Bypass Violations (Qty)", 
    "6. Machine Downtime (Minutes)", 
    "7. MTTR (Minutes)",
    "8. Skilled Technician Deployment (%)", 
    "9. Daily Checksheet / PM (%)",
    "10. BGA Yield [Line 1]", "10. BGA Yield [Line 2]", "10. BGA Yield [Line 3]",
    "11. RCAM Yield [Line 1]", "11. RCAM Yield [Line 2]", "11. RCAM Yield [Line 3]",
    "12. Line Output Achievement (Qty)", 
    "Last Edited Date", "Last Edited Time"
]

if not os.path.exists(database_filename):
    pd.DataFrame(columns=headers).to_csv(database_filename, index=False)

# =======================================================================================
# FLOATING COMPANY LOGO CONFIGURATION (RIGHT TOP MOUNT)
# =======================================================================================
logo_path = "logo.png" 

if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <div style="position: absolute; top: -60px; right: 10px; z-index: 999;">
            <img src="data:image/png;base64,{encoded_logo}" width="150">
        </div>
        """,
        unsafe_allow_html=True
    )

# Main Screen Title
st.title("📊 V57 Inspection Line Shift Leaders KPI Dashboard")
st.markdown("---")

# =======================================================================================
# STEP 1: SIDEBAR DATA ENTRY FORM
# =======================================================================================
st.sidebar.header("📝 DAILY KPI DATA ENTRY")
st.sidebar.caption("⚠️ Note: All fields are mandatory. Only numerical inputs are accepted.")

with st.sidebar.form(key='kpi_form', clear_on_submit=True):
    engineer_name = st.selectbox('👤 Engineer Name', ['Prathap', 'Lokesh', 'Ragav', 'Madhan', 'Thyagarajan', 'Umabathi', 'Naveen', 'Venkatesan'])
    shift_selection = st.selectbox('🕒 Shift', ['A', 'B', 'C', 'General'])
    selected_date = st.date_input('📅 Date', datetime.date.today())
    
    st.markdown("---")
    kpi_inputs = {}
    
    kpi_inputs["1. Safety Incidents (Qty)"] = st.number_input("1. Safety Incidents (Qty)", min_value=0, value=0, step=1)
    kpi_inputs["2. 5S Audit Score (%)"] = st.number_input("2. 5S Audit Score (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
    kpi_inputs["3. Near Miss / Suggestions (Qty)"] = st.number_input("3. Near Miss / Suggestions (Qty)", min_value=0, value=0, step=1)
    kpi_inputs["4. Kaizen Raised vs Closed (Qty)"] = st.number_input("4. Kaizen Raised vs Closed (Qty)", min_value=0, value=0, step=1)
    kpi_inputs["5. Zero Bypass Violations (Qty)"] = st.number_input("5. Zero Bypass Violations (Qty)", min_value=0, value=0, step=1)
    kpi_inputs["6. Machine Downtime (Minutes)"] = st.number_input("6. Machine Downtime (Minutes)", min_value=0, value=0, step=1)
    kpi_inputs["7. MTTR (Minutes)"] = st.number_input("7. MTTR (Minutes)", min_value=0, value=0, step=1)
    kpi_inputs["8. Skilled Technician Deployment (%)"] = st.number_input("8. Skilled Technician Deployment (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
    kpi_inputs["9. Daily Checksheet / PM (%)"] = st.number_input("9. Daily Checksheet / PM (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
        
    st.markdown("##### 10. Yield - BGA AOI First Pass (%)")
    kpi_inputs["10. BGA Yield [Line 1]"] = st.number_input("↳ BGA Line 1 (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
    kpi_inputs["10. BGA Yield [Line 2]"] = st.number_input("↳ BGA Line 2 (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
    kpi_inputs["10. BGA Yield [Line 3]"] = st.number_input("↳ BGA Line 3 (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")

    st.markdown("##### 11. Yield - RCAM AOI First Pass (%)")
    kpi_inputs["11. RCAM Yield [Line 1]"] = st.number_input("↳ RCAM Line 1 (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
    kpi_inputs["11. RCAM Yield [Line 2]"] = st.number_input("↳ RCAM Line 2 (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")
    kpi_inputs["11. RCAM Yield [Line 3]"] = st.number_input("↳ RCAM Line 3 (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0, format="%.0f")

    kpi_inputs["12. Line Output Achievement (Qty)"] = st.number_input("12. Line Output Achievement (Qty)", min_value=0, value=0, step=1)
    
    submit_button = st.form_submit_button(label='💾 Save KPI Entry')

if submit_button:
    now = datetime.datetime.now()
    row_dict = {
        "Date": str(selected_date), "Engineer Name": engineer_name, "Shift": shift_selection,
        "Last Edited Date": now.strftime("%Y-%m-%d"), "Last Edited Time": now.strftime("%I:%M:%S %p")
    }
    for lbl, val in kpi_inputs.items(): row_dict[lbl] = val
    
    # Save precisely keeping explicit order rules mapped
    save_df = pd.DataFrame([row_dict])
    save_df = save_df[[c for c in headers if c in save_df.columns]]
    save_df.to_csv(database_filename, mode='a', header=not os.path.exists(database_filename), index=False)
    st.sidebar.success("🎉 KPI Records updated!")
    st.rerun()

# Load Database & Strictly Realign Schema Columns
try:
    df = pd.read_csv(database_filename)
    
    # Force alignment block to strictly fix column shifts
    for col in headers:
        if col not in df.columns:
            df[col] = "N/A"
    df = df[headers]
    
    df_raw = df.copy()
    df_raw["Last Edited Date"] = df_raw["Last Edited Date"].fillna("N/A")
    df_raw["Last Edited Time"] = df_raw["Last Edited Time"].fillna("N/A")
    df['Date'] = pd.to_datetime(df['Date']).dt.date
except:
    df = pd.DataFrame(columns=headers)
    df_raw = df.copy()

# =======================================================================================
# VISUALIZATION & LOGS ENGINE
# =======================================================================================
if not df.empty:
    # FILTERS SYSTEM
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)
    with f_col1: 
        unique_engineers = df['Engineer Name'].dropna().astype(str).unique()
        all_engs = ['All Engineers'] + sorted(list(unique_engineers))
        sel_eng = st.selectbox('👤 Select Engineer:', all_engs)
        
    with f_col2: sel_dates = st.date_input('📅 Select Date:', [df['Date'].min(), df['Date'].max()])
    with f_col3: sel_line = st.selectbox('⚙️ Select Line:', ['All Lines', 'Line 1', 'Line 2', 'Line 3'])
    with f_col4: sel_shift = st.selectbox('🕒 Select Shift:', ['All Shifts'] + sorted(list(df['Shift'].dropna().astype(str).unique())))

    f_df = df.copy()
    if len(sel_dates) == 2:
        f_df = f_df[(f_df['Date'] >= sel_dates[0]) & (f_df['Date'] <= sel_dates[1])]
    if sel_eng != 'All Engineers': f_df = f_df[f_df['Engineer Name'] == sel_eng]
    if sel_shift != 'All Shifts': f_df = f_df[f_df['Shift'] == sel_shift]

    if not f_df.empty:
        numeric_cols = [c for c in f_df.columns if any(x in c for x in ["Qty", "%", "Minutes", "Yield"])]
        for col in numeric_cols: f_df[col] = pd.to_numeric(f_df[col], errors='coerce').fillna(0)

        # SCORECARD GRID
        st.subheader("📋 KPI Summary Overview")
        c1, c2, c3, c4 = st.columns(4)
        
        c1.metric("Total Safety Issues", f"{int(f_df['1. Safety Incidents (Qty)'].sum())} Qty")
        c1.metric("Average 5S Score", f"{round(f_df['2. 5S Audit Score (%)'].mean(), 1)}%")
        c1.metric("Total Near Misses", f"{int(f_df['3. Near Miss / Suggestions (Qty)'].sum())} Qty")
        
        c2.metric("Total Kaizens Closed", f"{int(f_df['4. Kaizen Raised vs Closed (Qty)'].sum())} Qty")
        c2.metric("Total Bypass Violations", f"{int(f_df['5. Zero Bypass Violations (Qty)'].sum())} Qty")
        c2.metric("Total Downtime", f"{int(f_df['6. Machine Downtime (Minutes)'].sum()):,} Mins")
        
        c3.metric("Average MTTR Score", f"{int(round(f_df['7. MTTR (Minutes)'].mean()))} Mins")
        c3.metric("Total Tech Deployment", f"{round(f_df['8. Skilled Technician Deployment (%)'].mean(), 1)}%")
        c3.metric("Total PM Compliance", f"{round(f_df['9. Daily Checksheet / PM (%)'].mean(), 1)}%")
        
        avg_bga = round(f_df[[c for c in f_df.columns if "10. BGA" in c]].mean().mean(), 2)
        avg_rcam = round(f_df[[c for c in f_df.columns if "11. RCAM" in c]].mean().mean(), 2)
        c4.metric("Avg BGA Yield", f"{avg_bga}%")
        c4.metric("Avg RCAM Yield", f"{avg_rcam}%")
        c4.metric("Total Line Output", f"{int(f_df['12. Line Output Achievement (Qty)'].sum()):,} Qty")

        st.markdown("---")
        
        # GRAPHICAL TREND ANALYSIS
        st.subheader("📊 Graphical Trend Analysis")
        
        actual_numeric_cols = [c for c in numeric_cols if c not in ['Date', 'Shift']]

        if sel_eng == 'All Engineers':
            graph_df = f_df.groupby('Date', as_index=False)[actual_numeric_cols].mean()
            dates_x = [str(d) for d in graph_df['Date'].tolist()]
            chart_title_suffix = "(Daily Team Average)"
        else:
            graph_df = f_df.groupby(['Date', 'Shift'], as_index=False)[actual_numeric_cols].mean()
            dates_x = [f"{r['Date']} (Sh-{r['Shift']})" for _, r in graph_df.iterrows()]
            chart_title_suffix = f"- {sel_eng}"

        lines = ['Line 1', 'Line 2', 'Line 3'] if sel_line == 'All Lines' else [sel_line]
        corporate_palette = ['#0f172a', '#2563eb', '#94a3b8']
        
        ch1, ch2 = st.columns(2)
        
        with ch1:
            fig_b = go.Figure()
            for idx, l in enumerate(lines):
                col_name = f"10. BGA Yield [{l}]"
                if col_name in graph_df.columns:
                    y_data = graph_df[col_name].round(2)
                    fig_b.add_trace(go.Bar(x=dates_x, y=y_data, name=l, text=y_data, textposition='outside', marker_color=corporate_palette[idx % 3]))
            fig_b.update_layout(title=f"<b>BGA Yield First Pass (%) {chart_title_suffix}</b>", template="plotly_white", barmode='group', yaxis=dict(range=[0, 115]), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
            st.plotly_chart(fig_b, use_container_width=True)

        with ch2:
            fig_r = go.Figure()
            for idx, l in enumerate(lines):
                col_name = f"11. RCAM Yield [{l}]"
                if col_name in graph_df.columns:
                    y_data = graph_df[col_name].round(2)
                    fig_r.add_trace(go.Bar(x=dates_x, y=y_data, name=l, text=y_data, textposition='outside', marker_color=corporate_palette[idx % 3]))
            fig_r.update_layout(title=f"<b>RCAM Yield First Pass (%) {chart_title_suffix}</b>", template="plotly_white", barmode='group', yaxis=dict(range=[0, 115]), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
            st.plotly_chart(fig_r, use_container_width=True)

        # KPI EXCEL PREVIEW
        st.header("📊 KPI Excel Preview")
        excel_display_df = f_df[[c for c in headers if c in f_df.columns]]
        st.dataframe(excel_display_df, use_container_width=True)

        # DATABASE EDITOR
        st.markdown("---")
        st.header("⚙️ Live Database Editor & Deleter")
        st.write("• **To Edit:** Double-click any cell and change values.\n• **To Delete:** Select a row using the checkbox on the left side and press the **`Delete`** key on your keyboard.")
        
        # Lock visual grid representation structural sequence
        available_headers = [c for c in headers if c in df_raw.columns]
        df_raw_aligned = df_raw[available_headers]
        
        edited_df = st.data_editor(
            df_raw_aligned, 
            use_container_width=True, 
            num_rows="dynamic",
            disabled=["Last Edited Date", "Last Edited Time"],
            key="db_editor"
        )
        
        if st.button("💾 Save Changes to Database", type="primary"):
            now = datetime.datetime.now()
            current_date = now.strftime("%Y-%m-%d")
            current_time = now.strftime("%I:%M:%S %p")
            
            final_rows = []
            for index, row in edited_df.iterrows():
                row_dict = row.to_dict()
                
                if index in df_raw_aligned.index:
                    orig_clean = df_raw_aligned.loc[index].drop(["Last Edited Date", "Last Edited Time"])
                    curr_clean = row.drop(["Last Edited Date", "Last Edited Time"])
                    
                    if not curr_clean.equals(orig_clean):
                        row_dict["Last Edited Date"] = current_date
                        row_dict["Last Edited Time"] = current_time
                else:
                    row_dict["Last Edited Date"] = current_date
                    row_dict["Last Edited Time"] = current_time
                    
                final_rows.append(row_dict)
            
            if final_rows:
                output_df = pd.DataFrame(final_rows)
                output_df = output_df[[c for c in headers if c in output_df.columns]]
            else:
                output_df = pd.DataFrame(columns=headers)
                
            output_df.to_csv(database_filename, index=False)
            st.success("Successfully synchronized global entries and timestamp hashes!")
            st.rerun()
    else:
        st.warning("No tracked items match parameters.")
else:
    st.info("⚠️ Dashboard Engine active. Submit entries via the side panel.")

# =======================================================================================
# STEP 3: PROFESSIONAL DEDICATED FIXED FOOTER REGISTRATION
# =======================================================================================
st.markdown(
    """
    <div class="corporate-footer">
        Developed by Ramesh Reddy (G0191) &nbsp;&bull;&nbsp; Maintenance Department
    </div>
    """,
    unsafe_allow_html=True
)