from database import get_connection
from datetime import date

# TOOL 1: Log Interaction
def log_interaction_tool(data: dict):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO interactions 
        (hcp_id, date, interaction_type, products_discussed, summary, follow_up_date)
        VALUES (1, CURRENT_DATE, %s, %s, %s, %s)
        """,
        (
            data.get("interaction_type", "visit"),
            data.get("product", ""),
            data.get("summary", ""),
            data.get("follow_up", None),
        ),
    )

    conn.commit()
    cur.close()
    conn.close()
    return "Interaction logged successfully"


# TOOL 2: Edit Interaction
def edit_interaction_tool(interaction_id: int, new_date: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "UPDATE interactions SET follow_up_date=%s WHERE id=%s",
        (new_date, interaction_id),
    )

    conn.commit()
    cur.close()
    conn.close()
    return "Interaction updated successfully"


# TOOL 3: Get HCP Profile
def get_hcp_profile():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM hcps LIMIT 1")
    data = cur.fetchone()

    cur.close()
    conn.close()
    return str(data)


# TOOL 4: Interaction Summary
def interaction_summary_tool():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT summary FROM interactions ORDER BY id DESC LIMIT 5")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return str(data)


# TOOL 5: Next Best Action
def next_best_action_tool():
    return "Recommended: Send product samples and schedule follow-up visit."