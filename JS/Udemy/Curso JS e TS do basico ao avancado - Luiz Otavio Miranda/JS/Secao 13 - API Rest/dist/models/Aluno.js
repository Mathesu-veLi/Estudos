"use strict";Object.defineProperty(exports, "__esModule", {value: true}); function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }var _sequelize = require('sequelize'); var _sequelize2 = _interopRequireDefault(_sequelize);

 class Aluno extends _sequelize.Model {
  static init(sequelize) {
    super.init({
      nome: {
        type: _sequelize2.default.STRING,
        defaultValue: '',
        validade: {
          len: {
            args: [3, 255],
            msg: 'Nome precisa ter entre 3 e 255 caracteres'
          },
        },
      },

      sobrenome: {
        type: _sequelize2.default.STRING,
        defaultValue: '',
        validade: {
          len: {
            args: [3, 255],
            msg: 'Sobrenome precisa ter entre 3 e 255 caracteres'
          },
        },
      },

      email: {
        type: _sequelize2.default.STRING,
        defaultValue: '',
        validate: {
          isEmail: {
            msg: 'Email inválido'
          },

          isUnique(value, next) {
            Aluno.findOne({ where: { email: value } }).then(aluno => {
              if (aluno) {
                return next('Email já existe, tente outro!');
              };
              return next();
            }).catch(err => next(err));
          },

        },
      },

      idade: {
        type: _sequelize2.default.INTEGER,
        defaultValue: '',
        validade: {
          isInt: {
            msg: 'Idade precisa ser um número inteiro'
          },
        },
      },

      peso: {
        type: _sequelize2.default.FLOAT,
        defaultValue: '',
        validade: {
          isFloat: {
            msg: 'Peso precisa ser um número inteiro ou flutuante'
          },
        },
      },

      altura: {
        type: _sequelize2.default.FLOAT,
        defaultValue: '',
        validade: {
          isFloat: {
            msg: 'Altura precisa ser um número inteiro ou flutuante'
          },
        },
      },

      created_by: {
        type: _sequelize2.default.STRING,
        defaultValue: ''
      }
    }, {
      sequelize,
    });

    this.addHook('beforeSave', (aluno, userId) => aluno.created_by = userId);
    return this;
  };

  static associate(models) {
    this.hasMany(models.Photo, { foreignKey: 'aluno_id'})
  }
} exports.default = Aluno;
