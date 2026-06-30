def retrieve_by_aspect(
    transcript,
    aspect,
    threshold=0.5
):

    filtered = []

    for qa in transcript:

        if qa["weights"][aspect] >= threshold:

            filtered.append(qa)

    return filtered