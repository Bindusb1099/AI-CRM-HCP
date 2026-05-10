from database import get_connection
from datetime import date
import json

# =========================
# TOOL 1: Log Interaction
# =========================
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

    return "✅ Interaction logged successfully"


# =========================
# TOOL 2: Edit Interaction
# =========================
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

    return "✅ Interaction updated successfully"


# =========================
# TOOL 3: Get HCP Profile
# =========================
def get_hcp_profile():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, specialty, hospital, city FROM hcps LIMIT 1")
    data = cur.fetchone()

    cur.close()
    conn.close()

    if data is None:
        return "❌ No HCP profile found in database"

    result = {
        "id": data[0],
        "name": data[1],
        "specialty": data[2],
        "hospital": data[3],
        "city": data[4],
    }

    return json.dumps(result)


# =========================
# TOOL 4: Interaction Summary
# =========================
def interaction_summary_tool():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT summary FROM interactions ORDER BY id DESC LIMIT 5")
    data = cur.fetchall()

    cur.close()
    conn.close()

    if not data:
        return "❌ No interaction summaries found"

    summaries = [row[0] for row in data]

    return json.dumps({
        "recent_summaries": summaries
    })


# =========================
# TOOL 5: Next Best Action
# =========================
def next_best_action_tool():
    return json.dumps({
        "recommendation": "Send product samples and schedule follow-up visit with HCP."
    })