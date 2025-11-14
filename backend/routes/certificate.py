from flask import Blueprint, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User, Attempt
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from datetime import datetime
import io
import os

certificate_bp = Blueprint('certificate', __name__)

def generate_certificate_pdf(user_name, role, score, date):
    """Generate a PDF certificate mirroring the frontend design."""
    buffer = io.BytesIO()
    page_size = landscape(A4)
    c = canvas.Canvas(buffer, pagesize=page_size)
    width, height = page_size

    # Color palette
    primary = colors.HexColor('#009edb')
    primary_dark = colors.HexColor('#0075a4')
    primary_light = colors.HexColor('#e0f7ff')
    badge_gold = colors.HexColor('#f5c242')
    slate_800 = colors.HexColor('#1f2933')

    # Background (white to match frontend page)
    c.setFillColor(colors.white)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Card container
    card_margin = 45
    corner_radius = 18
    card_width = width - (card_margin * 2)
    card_height = height - (card_margin * 2)

    c.setFillColor(colors.white)
    c.roundRect(card_margin, card_margin, card_width, card_height, corner_radius, fill=1, stroke=0)

    # Outer border
    c.setStrokeColor(primary)
    c.setLineWidth(4)
    c.roundRect(card_margin, card_margin, card_width, card_height, corner_radius, fill=0, stroke=1)

    # Subtle inner border
    c.setStrokeColor(primary_light)
    c.setLineWidth(2)
    inner_margin = card_margin + 12
    c.roundRect(inner_margin, inner_margin, width - (inner_margin * 2), height - (inner_margin * 2), corner_radius, fill=0, stroke=1)

    # Watermark logo
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    logo_path = os.path.join(project_root, 'frontend', 'public', 'logo-website.png')
    if os.path.exists(logo_path):
        try:
            logo = ImageReader(logo_path)
            logo_width_px, logo_height_px = logo.getSize()
            desired_width = card_width * 0.65
            aspect_ratio = logo_height_px / logo_width_px if logo_width_px else 1
            desired_height = desired_width * aspect_ratio
            logo_x = (width - desired_width) / 2
            logo_y = (height - desired_height) / 2

            c.saveState()
            if hasattr(c, 'setFillAlpha'):
                c.setFillAlpha(0.12)
            c.drawImage(
                logo,
                logo_x,
                logo_y,
                width=desired_width,
                height=desired_height,
                mask='auto',
                preserveAspectRatio=True
            )
            c.restoreState()
        except Exception:
            pass

    # Header text
    header_y = height - card_margin - 60
    c.setFillColor(primary)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(width / 2, header_y, "CERTIFICATE")

    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(slate_800)
    c.drawCentredString(width / 2, header_y - 42, "OF ACHIEVEMENT")

    # Divider line
    c.setStrokeColor(primary)
    c.setLineWidth(2)
    c.line(width / 2 - 110, header_y - 65, width / 2 + 110, header_y - 65)

    # Body copy
    body_top = header_y - 120
    c.setFillColor(slate_800)
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, body_top, "This is to certify that")

    c.setFont("Helvetica-Bold", 30)
    c.setFillColor(primary_dark)
    c.drawCentredString(width / 2, body_top - 45, user_name.upper())

    # Underline accent
    c.setStrokeColor(primary)
    c.setLineWidth(1.5)
    underline_width = 240
    c.line((width - underline_width) / 2, body_top - 55, (width + underline_width) / 2, body_top - 55)

    c.setFillColor(slate_800)
    c.setFont("Helvetica", 16)
    c.drawCentredString(width / 2, body_top - 95, "has successfully completed the")

    c.setFillColor(primary)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(width / 2, body_top - 135, f"{role} Certification Test")

    # Score card
    score_box_width = 220
    score_box_height = 50
    score_box_x = (width - score_box_width) / 2
    score_box_y = body_top - 210
    score_bg = colors.HexColor('#bbf7d0')  # Tailwind green-100 equivalent
    score_text = colors.HexColor('#047857')
    c.setFillColor(score_bg)
    c.roundRect(score_box_x, score_box_y, score_box_width, score_box_height, 14, fill=1, stroke=0)
    c.setStrokeColor(score_bg)
    c.setLineWidth(1)
    c.roundRect(score_box_x, score_box_y, score_box_width, score_box_height, 14, fill=0, stroke=1)

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(score_text)
    c.drawCentredString(width / 2, score_box_y + (score_box_height / 2) - 5, f"Score: {score}/10")

    # Date label
    c.setFont("Helvetica", 14)
    c.setFillColor(slate_800)
    c.drawCentredString(width / 2, score_box_y - 45, f"Date: {date}")

    # Badge
    badge_radius = 40
    badge_center_x = width - card_margin - badge_radius - 15
    badge_center_y = height - card_margin - badge_radius - 15
    c.setFillColor(badge_gold)
    c.circle(badge_center_x, badge_center_y, badge_radius, stroke=0, fill=1)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(badge_center_x, badge_center_y + 6, "✓")
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(badge_center_x, badge_center_y - 14, "CERTIFIED")

    # Footer note
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.HexColor('#6b7280'))
    c.drawCentredString(width / 2, card_margin + 30, "This certificate is generated digitally and does not require a physical signature.")

    c.showPage()
    c.save()

    buffer.seek(0)
    return buffer

@certificate_bp.route('/certificate/<int:user_id>', methods=['GET'])
@jwt_required()
def get_certificate(user_id):
    """Get certificate data for a user"""
    try:
        current_user_id = int(get_jwt_identity())
        
        # Verify user can only access their own certificate
        if current_user_id != user_id:
            return jsonify({'error': 'Unauthorized access'}), 403
        
        # Get user
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Get passed attempt
        passed_attempt = Attempt.query.filter_by(
            user_id=user_id, 
            passed=True
        ).order_by(Attempt.timestamp.desc()).first()
        
        if not passed_attempt:
            return jsonify({
                'error': 'No passed attempt found',
                'has_certificate': False
            }), 404
        
        # Return certificate data
        return jsonify({
            'has_certificate': True,
            'name': user.name,
            'role': user.role,
            'score': passed_attempt.score,
            'date': passed_attempt.timestamp.strftime('%B %d, %Y'),
            'attempt_number': passed_attempt.attempt_number
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@certificate_bp.route('/certificate/<int:user_id>/download', methods=['GET'])
@jwt_required()
def download_certificate(user_id):
    """Download certificate as PDF"""
    try:
        current_user_id = int(get_jwt_identity())
        
        # Verify user can only download their own certificate
        if current_user_id != user_id:
            return jsonify({'error': 'Unauthorized access'}), 403
        
        # Get user
        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        # Get passed attempt
        passed_attempt = Attempt.query.filter_by(
            user_id=user_id, 
            passed=True
        ).order_by(Attempt.timestamp.desc()).first()
        
        if not passed_attempt:
            return jsonify({'error': 'No passed attempt found'}), 404
        
        # Generate PDF
        pdf_buffer = generate_certificate_pdf(
            user.name,
            user.role,
            passed_attempt.score,
            passed_attempt.timestamp.strftime('%B %d, %Y')
        )
        
        # Return PDF file
        return send_file(
            pdf_buffer,
            as_attachment=True,
            download_name=f'certificate_{user.name.replace(" ", "_")}.pdf',
            mimetype='application/pdf'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
