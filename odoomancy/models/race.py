from odoo import models, fields

class OdoomancyRace(models.Model):
    _name = "odoomancy.race"
    _description = "Race"

    name = fields.Char(string='Name', required=True)
    index = fields.Char(string='Index', readonly=True)
    speed = fields.Integer(string='Speed (ft)')
    ability_bonus_ids = fields.One2many(
        'odoomancy.race.ability.bonus', 'race_id', string='Ability Bonuses'
    )
    alignment = fields.Text(string='Alignment')
    age = fields.Text(string='Age')
    size = fields.Selection([
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ], string='Size')
    size_description = fields.Text(string='Size Description')
    language_ids = fields.Many2many(
        'odoomancy.race.language', string='Languages')
    language_description = fields.Text(string='Language Description')
    trait_ids = fields.One2many(
        'odoomancy.race.trait', 'race_id', string='Traits'
    )
    subrace_ids = fields.One2many(
        'odoomancy.subrace', 'race_id', string='Subraces'
    )

class OdoomancyRaceAbilityBonus(models.Model):
    _name = 'odoomancy.race.ability.bonus'
    _description = 'Race Ability Bonus'

    race_id = fields.Many2one(
        'odoomancy.race',
        string='Race',
        required=True,
        ondelete='cascade'
    )
    ability_score_id = fields.Many2one(
        'odoomancy.ability.score',
        string='Ability Score',
        required=True
    )
    bonus = fields.Integer(string='Bonus')

class OdoomancyRaceLanguage(models.Model):
    _name = 'odoomancy.race.language'
    _description = 'Race Language'

    name = fields.Char(string='Language', required=True)
    index = fields.Char(string='Index', readonly=True)
    description = fields.Text(string='Description')
    type_language = fields.Selection([
        ('Exotic', 'Exotic'),
        ('Standard', 'Standard')
    ], string='Type')
    typical_speaker_ids = fields.Many2many(
        'odoomancy.race.speaker',
        string='Typical Speakers'
    )
    script = fields.Char(string='Script')
    race_ids = fields.Many2many(
        'odoomancy.race',
        string='Races')


class OdoomancyRaceSpeaker(models.Model):
    _name = 'odoomancy.race.speaker'
    _description = 'Typical Speaker'

    name = fields.Char(string='Name', required=True)
    language_ids = fields.Many2many(
        'odoomancy.race.language',
        string='Languages'
    )

class OdoomancyTrait(models.Model):
    _name = 'odoomancy.race.trait'
    _description = 'Trait'

    name = fields.Char(string='Name', required=True)
    index = fields.Char(string='API Index', required=True)
    description = fields.Text(string='Description')
    race_ids = fields.Many2many(
        'odoomancy.race',
        string='Races'
    )
    subrace_ids = fields.Many2many(
        'odoomancy.subrace',
        string='Subraces'
    )
    proficiency_ids = fields.Many2many(
        'odoomancy.proficiency',
        string='Proficiencies'
    )
    subtrait_choose = fields.Integer(string='Choose N subtraits')
    subtrait_ids = fields.One2many(
        'odoomancy.race.trait.subtrait',
        'trait_id',
        string='Subtrait Options'
    )

class OdoomancyTraitSubtrait(models.Model):
    _name = 'odoomancy.race.trait.subtrait'
    _description = 'Trait Subtrait'

    name = fields.Char(string='Name', required=True)
    index = fields.Char(string='API Index', required=True)
    description = fields.Text(string='Description')
    trait_id = fields.Many2one(
        'odoomancy.race.trait',
        string='Parent Trait',
        required=True,
        ondelete='cascade'
    )
    race_ids = fields.Many2many(
        'odoomancy.race',
        string='Races'
    )
    subrace_ids = fields.Many2many(
        'odoomancy.subrace',
        string='Subraces'
    )
    proficiency_ids = fields.Many2many(
        'odoomancy.proficiency',
        string='Proficiencies'
    )
    # TODO:futuro modelo
    # damage_type_id = fields.Many2one(
    #     'odoomancy.damage.type',
    #     string='Damage Type'
    # )
    # TODO:futuro modelo
    # breath_weapon_id = fields.Many2one(
    #     'odoomancy.breath.weapon',
    #     string='Breath Weapon'
    # )

# TODO: Quiza mejor separarlo en otro archivo ya que se va usar mucho (Check with Juanlu)
class OdoomancyProficiency(models.Model):
    _name = 'odoomancy.proficiency'
    _description = 'Proficiency'

    name = fields.Char(string='Name', required=True)
    index = fields.Char(string='API Index', required=True)
    type_proficiency = fields.Selection([
        ('Weapons', 'Weapons'),
        ('Armor', 'Armor'),
        ('Artisans Tools', "Artisan's Tools"),
        ('Skills', 'Skills'),
        ('Saving Throws', 'Saving Throws'),
        ('Other', 'Other'),
    ], string='Type')
    race_ids = fields.Many2many(
        'odoomancy.race',
        string='Races'
    )
    # TODO:futuro modelo
    # class_ids = fields.Many2many(
    #     'odoomancy.class',
    #     string='Classes'
    # )

    # TODO: Revisar esta parte es un poco compleja
    reference = fields.Reference(
        selection=[
            ('odoomancy.equipment', 'Equipment'),
            ('odoomancy.equipment.category', 'Equipment Category'),
            ('odoomancy.skill', 'Skill'),
            ('odoomancy.ability.score', 'Ability Score'),
        ],
        string='Reference'
    )

class OdoomancySubrace(models.Model):
    _name = 'odoomancy.subrace'
    _description = 'Subrace'

    name = fields.Char(string='Name', required=True)
    index = fields.Char(string='Index', readonly=True)
    race_id = fields.Many2one(
        'odoomancy.race', string='Race', ondelete='cascade')
    description = fields.Text(string='Description')
    ability_bonus_ids = fields.One2many(
        'odoomancy.race.ability.bonus',
        'subrace_id',
        string='Ability Bonuses'
    )
    trait_ids = fields.One2many(
        'odoomancy.race.trait',
        'subrace_id',
        string='Racial Traits'
    )
