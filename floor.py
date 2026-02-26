import streamlit.components.v1 as components

def render_floor(selected_zone, overlay_color):

    def zone_block(name, width, height):
        if name == selected_zone and overlay_color:
            bg = overlay_color
        else:
            bg = "rgba(220,220,220,0.5)"

        return f"""
        <div style="
            background:{bg};
            border:1px solid #999;
            border-radius:8px;
            width:{width};
            height:{height};
            display:flex;
            align-items:center;
            justify-content:center;
            text-align:center;
            font-size:13px;
            padding:6px;
        ">
            {name}
        </div>
        """

    floor_html = f"""
    <div style="
        width:100%;
        height:600px;
        background:#f5f5f5;
        border:2px solid #ccc;
        border-radius:12px;
        display:flex;
        padding:20px;
        gap:20px;
        box-sizing:border-box;
    ">

        <!-- WEST -->
        <div style="flex:1; display:flex; flex-direction:column; gap:20px;">
            {zone_block("Z1 - Silent Study Core", "100%", "100%")}
        </div>

        <!-- CENTER -->
        <div style="flex:2; display:flex; flex-direction:column; gap:20px;">
            {zone_block("Z2 - Scenic Lake View Window", "100%", "30%")}
            {zone_block("Z3 - Open Table Collaborative Center", "100%", "70%")}
        </div>

        <!-- EAST -->
        <div style="flex:1; display:flex; flex-direction:column; gap:20px;">
            {zone_block("Z5 - Premium Scenic Media Studios (2252A/B)", "100%", "30%")}
            {zone_block("Z4 - Computer & Media Center", "100%", "70%")}
        </div>

    </div>
    """

    components.html(floor_html, height=650)