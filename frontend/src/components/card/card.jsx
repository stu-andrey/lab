import styles from './card.module.css';
import { WORKS_IMAGES_URL } from '../../utils/works-api';

function Card({work, handleModal}) {
    return (
      <div className={styles.card}>
        <img className={styles.image} src={WORKS_IMAGES_URL + work.image} />
      </div>
    );
  }
  
  export default Card;
  