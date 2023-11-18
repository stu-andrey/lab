import { useState, useEffect } from 'react';

import Card from '../card/card';

import { getWorks } from '../../utils/works-api';

import styles from "./app.module.css";

function App() {

  const [works, setWorks] = useState({});

  useEffect(() => {
    setWorks({...works, isLoading: true});
    getWorks()
      .then(data => setWorks({...works, data: data, isLoading: false, hasError: false}))
      .catch(e => setWorks({...works, isLoading: false, hasError: true}));
  }, []);

  // useEffect(() => {
  //   setActiveWork({...activeWork, isLoading: true});
  //   getWorkById()
  //     .then(data => setWorks({...activeWork, data: data, isLoading: false, hasError: false}))
  //     .catch(e => setWorks({...activeWork, isLoading: false, hasError: true}));
  // }, []);

  // console.log(works);

  return (
    <>
      <div className={styles.page}>
        <div className={styles.cards}>
          {
            works.data && works.data.map(work => 
              <Card key={work.id} work={work} />
            )
          }
        </div>
      </div>

    </>
  );
}

export default App;
