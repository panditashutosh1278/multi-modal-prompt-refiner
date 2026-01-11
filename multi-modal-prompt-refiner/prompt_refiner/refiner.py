def refine_prompt(input_data):
    content = input_data.get("content", "").lower()
    modality = input_data.get("type", "unknown")

    output = {
        "intent_hypothesis": {
            "primary_intent": "",
            "confidence_score": 0.2,
            "justification": []
        },
        "requirements": {
            "functional": [],
            "non_functional": []
        },
        "constraints": {
            "technical": [],
            "business": []
        },
        "deliverables": [],
        "assumptions": [],
        "open_questions": [],
        "evidence_map": {
            "text": [],
            "image": [],
            "document": []
        },
        "refinement_metadata": {
            "completeness_level": "low",
            "ready_for_downstream_ai": False
        }
    }

    if "app" in content:
        output["intent_hypothesis"]["primary_intent"] = "Software Application Development"
        output["intent_hypothesis"]["confidence_score"] += 0.3
        output["intent_hypothesis"]["justification"].append(
            "Keyword 'app' detected in text input"
        )
        output["deliverables"].append("Application")
        output["evidence_map"][modality].append("Application intent inferred")

    if "task" in content:
        output["requirements"]["functional"].extend([
            "Task creation",
            "Task assignment",
            "Task tracking"
        ])
        output["intent_hypothesis"]["confidence_score"] += 0.2

    output["assumptions"].append(
        "Assumed collaborative usage based on task-related keywords"
    )

    output["open_questions"].extend([
        "Target platform (web or mobile)?",
        "Authentication required?",
        "Expected user scale?"
    ])

    if output["intent_hypothesis"]["confidence_score"] >= 0.6:
        output["refinement_metadata"]["completeness_level"] = "medium"
        output["refinement_metadata"]["ready_for_downstream_ai"] = True

    return output
