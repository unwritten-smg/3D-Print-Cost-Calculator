from flask import Blueprint, render_template, request, redirect, url_for
from app.logic.price_calculator import calculate_print_cost
from app.db.db import (
    get_materials, get_parts,
    save_material_if_new, save_part_if_new
)

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    selected_material = None
    selected_part = None

    materials = get_materials()
    parts = get_parts()

    if request.method == 'POST' and 'pages' in request.form:
        pages = int(request.form['pages'])
        copies = int(request.form['copies'])
        color = request.form['color']
        paper = request.form['paper']
        selected_material = request.form['material']
        selected_part = request.form['part']

        material_dict = dict(materials)
        part_dict = dict(parts)

        material_cost = material_dict.get(selected_material, 0)
        part_cost = part_dict.get(selected_part, 0)

        print_cost = calculate_print_cost(pages, copies, color, paper)
        total = print_cost + material_cost + part_cost

        result = {
            "print_cost": print_cost,
            "material_cost": material_cost,
            "part_cost": part_cost,
            "total": total
        }

    return render_template("index.html",
        materials=materials,
        parts=parts,
        result=result,
        selected_material=selected_material,
        selected_part=selected_part
    )

@main.route('/add_material', methods=['POST'])
def add_material():
    name = request.form['material_name']
    price = float(request.form['material_price'])
    save_material_if_new(name, price)
    return redirect(url_for('main.index'))

@main.route('/add_part', methods=['POST'])
def add_part():
    name = request.form['part_name']
    price = float(request.form['part_price'])
    save_part_if_new(name, price)
    return redirect(url_for('main.index'))
